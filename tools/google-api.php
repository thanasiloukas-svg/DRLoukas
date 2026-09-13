<?php
/**
 * Minimal Google API client for Loukas Dentistry.
 * Service-account (JWT) auth, no Composer, no external libraries.
 *
 * Credentials live in credentials.php in this directory, which returns the
 * service-account key as an array. That file is PHP, so an HTTP request for it
 * executes and returns nothing rather than leaking the key.
 *
 * Added 2026-08-30 so any Claude session can read Search Console directly
 * through Novamira, instead of depending on a local machine being switched on.
 */

defined('ABSPATH') || exit;

class Loukas_Google_API {

    const TOKEN_TRANSIENT = 'loukas_google_token_';

    private static function credentials() {
        $file = __DIR__ . '/credentials.php';
        if (!file_exists($file)) {
            return new WP_Error('no_credentials', 'credentials.php not found in ' . __DIR__);
        }
        $creds = include $file;
        if (!is_array($creds) || empty($creds['client_email']) || empty($creds['private_key'])) {
            return new WP_Error('bad_credentials', 'credentials.php did not return a valid service-account array');
        }
        return $creds;
    }

    private static function b64($data) {
        return rtrim(strtr(base64_encode($data), '+/', '-_'), '=');
    }

    /** Exchange the service-account key for an OAuth access token. Cached until shortly before expiry. */
    public static function token($scope) {
        $cache_key = self::TOKEN_TRANSIENT . md5($scope);
        $cached = get_transient($cache_key);
        if ($cached) {
            return $cached;
        }

        $creds = self::credentials();
        if (is_wp_error($creds)) {
            return $creds;
        }

        $now = time();
        $claim = array(
            'iss'   => $creds['client_email'],
            'scope' => $scope,
            'aud'   => 'https://oauth2.googleapis.com/token',
            'exp'   => $now + 3600,
            'iat'   => $now,
        );
        if (!empty($creds['impersonate'])) {
            $claim['sub'] = $creds['impersonate'];
        }

        $input = self::b64(json_encode(array('alg' => 'RS256', 'typ' => 'JWT')))
               . '.' . self::b64(json_encode($claim));

        $signature = '';
        if (!openssl_sign($input, $signature, $creds['private_key'], 'sha256WithRSAEncryption')) {
            return new WP_Error('sign_failed', 'Could not sign the JWT with the provided private key');
        }
        $jwt = $input . '.' . self::b64($signature);

        $res = wp_remote_post('https://oauth2.googleapis.com/token', array(
            'timeout' => 20,
            'body'    => array(
                'grant_type' => 'urn:ietf:params:oauth:grant-type:jwt-bearer',
                'assertion'  => $jwt,
            ),
        ));
        if (is_wp_error($res)) {
            return $res;
        }

        $body = json_decode(wp_remote_retrieve_body($res), true);
        if (empty($body['access_token'])) {
            $detail = isset($body['error_description']) ? $body['error_description'] : wp_remote_retrieve_body($res);
            return new WP_Error('token_failed', 'Token request failed: ' . substr($detail, 0, 300));
        }

        set_transient($cache_key, $body['access_token'], 3000);
        return $body['access_token'];
    }

    /** Generic authenticated JSON request. */
    public static function request($url, $scope, $payload = null, $method = 'GET') {
        $token = self::token($scope);
        if (is_wp_error($token)) {
            return $token;
        }

        $args = array(
            'method'  => $method,
            'timeout' => 45,
            'headers' => array(
                'Authorization' => 'Bearer ' . $token,
                'Content-Type'  => 'application/json',
            ),
        );
        if (null !== $payload) {
            $args['body']   = wp_json_encode($payload);
            $args['method'] = 'POST';
        }

        $res = wp_remote_request($url, $args);
        if (is_wp_error($res)) {
            return $res;
        }

        $code = wp_remote_retrieve_response_code($res);
        $body = json_decode(wp_remote_retrieve_body($res), true);
        if ($code >= 400) {
            $msg = isset($body['error']['message']) ? $body['error']['message'] : wp_remote_retrieve_body($res);
            return new WP_Error('api_' . $code, substr($msg, 0, 400));
        }
        return $body;
    }

    /* ---------------- Search Console ---------------- */

    const GSC_SCOPE = 'https://www.googleapis.com/auth/webmasters.readonly';
    const SITE      = 'https://www.drloukas.com/';

    /** List the properties this service account can see. Use this to verify access. */
    public static function gsc_sites() {
        return self::request('https://searchconsole.googleapis.com/webmasters/v3/sites', self::GSC_SCOPE);
    }

    /**
     * Search Analytics query.
     * $dimensions e.g. array('query'), array('page'), array('query','page'), array('date')
     */
    public static function gsc_query($start, $end, $dimensions = array('query'), $rowLimit = 100, $filters = array()) {
        $payload = array(
            'startDate'  => $start,
            'endDate'    => $end,
            'dimensions' => $dimensions,
            'rowLimit'   => $rowLimit,
        );
        if (!empty($filters)) {
            $payload['dimensionFilterGroups'] = array(array('filters' => $filters));
        }
        $url = 'https://searchconsole.googleapis.com/webmasters/v3/sites/'
             . rawurlencode(self::SITE) . '/searchAnalytics/query';
        return self::request($url, self::GSC_SCOPE, $payload);
    }

    /** URL Inspection for a single page. */
    public static function gsc_inspect($page_url) {
        $payload = array(
            'inspectionUrl' => $page_url,
            'siteUrl'       => self::SITE,
        );
        return self::request(
            'https://searchconsole.googleapis.com/v1/urlInspection/index:inspect',
            'https://www.googleapis.com/auth/webmasters',
            $payload
        );
    }

    /** Sitemaps list, including error/warning counts. */
    public static function gsc_sitemaps() {
        $url = 'https://searchconsole.googleapis.com/webmasters/v3/sites/'
             . rawurlencode(self::SITE) . '/sitemaps';
        return self::request($url, self::GSC_SCOPE);
    }
}
