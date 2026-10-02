<?php
defined('ABSPATH') || exit;

function loukas_setup() {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('html5', ['search-form', 'comment-form', 'comment-list', 'gallery', 'caption', 'style', 'script']);
    register_nav_menus(['primary' => 'Primary Menu']);
}
add_action('after_setup_theme', 'loukas_setup');

function loukas_enqueue() {
    $v = wp_get_theme()->get('Version');

    wp_enqueue_style('google-fonts',
        'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Source+Sans+3:wght@300;400;600;700&display=swap',
        [], null);

    wp_enqueue_style('loukas-main', get_template_directory_uri() . '/assets/css/main.css', [], $v);

    if (is_front_page()) {
        wp_enqueue_script('loukas-canvas', get_template_directory_uri() . '/assets/js/canvas.js', [], $v, ['strategy' => 'defer', 'in_footer' => true]);
    }

    wp_enqueue_script('loukas-main', get_template_directory_uri() . '/assets/js/main.js', [], $v, ['in_footer' => true]);
}
add_action('wp_enqueue_scripts', 'loukas_enqueue');

function loukas_phone()     { return '(847) 696-1919'; }
function loukas_phone_raw() { return '8476961919'; }

function loukas_fallback_menu() {
    echo '<ul class="nav-list">';
    echo '<li><a href="/">Home</a></li>';
    echo '<li><a href="/emergency-dentistry/">Emergency Dentistry</a></li>';
    echo '<li class="menu-item-has-children"><a href="/dental-services/">Dental Services</a>';
    echo '<ul class="sub-menu">';
    echo '<li><a href="/dental-implants/">Dental Implants</a></li>';
    echo '<li><a href="/invisalign-park-ridge/">Invisalign</a></li>';
    echo '<li><a href="/cosmetic-dentistry/porcelain-veneers/">Porcelain Veneers</a></li>';
    echo '<li><a href="/teeth-whitening/">Teeth Whitening</a></li>';
    echo '<li><a href="/restorative-dentistry/dental-crowns/">Dental Crowns</a></li>';
    echo '<li><a href="/root-canal/">Root Canals</a></li>';
    echo '<li><a href="/sedation-dentistry/">Sedation Dentistry</a></li>';
    echo '<li><a href="/sleep-apnea-snoring-treatment/">Sleep Apnea</a></li>';
    echo '<li><a href="/permanent-gold-teeth/">Gold Crowns</a></li>';
    echo '</ul></li>';
    echo '<li class="menu-item-has-children"><a href="/cosmetic-dentistry/">Cosmetic &amp; Med Spa</a>';
    echo '<ul class="sub-menu">';
    echo '<li><a href="/botox/">Botox &amp; Dysport</a></li>';
    echo '<li><a href="/lip-fillers-park-ridge/">Lip Fillers</a></li>';
    echo '<li><a href="/pdo-threads/">PDO Threads</a></li>';
    echo '<li><a href="/kybella/">Kybella</a></li>';
    echo '<li><a href="/botox-for-migraines-headaches-park-ridge-il/">Botox for Migraines</a></li>';
    echo '<li><a href="/facial-aesthetics/">Facial Aesthetics</a></li>';
    echo '</ul></li>';
    echo '<li><a href="/smile-gallery/">Smile Gallery</a></li>';
    echo '<li><a href="/our-office/">Our Office</a></li>';
    echo '<li><a href="/virtual-tour/">Virtual Tour</a></li>';
    echo '<li><a href="/blog/">Blog</a></li>';
    echo '<li><a href="/about-us/">About</a></li>';
    echo '<li><a href="/contact-us/">Contact</a></li>';
    echo '</ul>';
}


// ============================================================
// Service Page Fixes – Aug 2026
// ============================================================
function loukas_service_page_styles() {
  // Only run on single posts and pages (not homepage)
  if ( ! is_singular() || is_front_page() ) return;
  ?>
  <style id="loukas-service-styles">
    /* Hide date/meta on service pages (all single posts) */
    body.single .lk-post-meta { display:none !important; }
    body.single .lk-post-header { margin-bottom:4px; }

    /* Responsive content images */
    .lk-content img { max-width:100%; height:auto; display:block; }
    .lk-content figure img, .lk-content .wp-block-image img {
      width:100%; height:auto; border-radius:8px;
    }

    /* Typography for service pages */
    .lk-content h2 {
      font-family:'Playfair Display',Georgia,serif;
      font-size:clamp(20px,3vw,26px);
      color:#06202D; margin:36px 0 12px; line-height:1.3;
    }
    .lk-content h3 {
      font-family:'Playfair Display',Georgia,serif;
      font-size:clamp(17px,2.5vw,21px);
      color:#06202D; margin:28px 0 10px;
    }
    .lk-content p { font-size:16px; line-height:1.75; color:#365F6F; margin-bottom:18px; }
    .lk-content ul, .lk-content ol { padding-left:24px; margin-bottom:18px; }
    .lk-content li { font-size:16px; line-height:1.7; color:#365F6F; margin-bottom:6px; }
    .lk-content a { color:#18C6B3; }
    .lk-content a:hover { color:#14b3a2; }
    .lk-content strong { color:#06202D; }

    /* Layout */
    .lk-main { padding:40px 0 80px; }
    .lk-container-narrow { max-width:800px; margin:0 auto; padding:0 24px; }
    .lk-page-title {
      font-family:'Playfair Display',Georgia,serif;
      font-size:clamp(24px,4vw,36px);
      color:#06202D; line-height:1.25; margin-bottom:8px;
    }
    .lk-content figcaption {
      font-size:13px; color:#888; text-align:center;
      margin-top:6px; font-style:italic;
    }

    /* Page template (not single posts) */
    .lk-article.lk-page { max-width:900px; }
  </style>
  <?php
}
add_action( 'wp_head', 'loukas_service_page_styles', 20 );

// Load jQuery in the <head> so plugin scripts printed inside templates (e.g. Smash Balloon feeds) find it. Added 2026-08-23.
function loukas_jquery_in_head() { wp_enqueue_script('jquery'); }
add_action('wp_enqueue_scripts', 'loukas_jquery_in_head', 1);
// Keep jQuery out of Jetpack Boost's JS deferral/relocation so it stays in <head> (feeds printed in templates depend on it). Added 2026-08-23.
function loukas_jquery_boost_ignore($tag, $handle) { if (in_array($handle, ['jquery-core', 'jquery-migrate'], true) && strpos($tag, 'data-jetpack-boost') === false) { $tag = str_replace('<script ', '<script data-jetpack-boost="ignore" ', $tag); } return $tag; }
add_filter('script_loader_tag', 'loukas_jquery_boost_ignore', 10, 2);
// YouTube latest-uploads shortcode (RSS based). Added 2026-08-23.
$loukas_yt = WP_CONTENT_DIR . '/novamira-sandbox/loukas-youtube-feed.php';
if (file_exists($loukas_yt)) { require_once $loukas_yt; }


/**
 * Defer non-critical front-end scripts (added 2026-08-30).
 * Uses WordPress' native 'strategy' API, which refuses to defer a handle
 * when a dependent would break, so this is dependency-safe by design.
 */
function loukas_defer_frontend_scripts() {
    if ( is_admin() ) {
        return;
    }
    $handles = array(
        'react',
        'react-dom',
        'wp-element',
        'wp-escape-html',
        'underscore',
        'responsive-lightbox-front',
        'responsive-lightbox-sanitizer',
        'aioseo-gtm',
        'mwai_chatbot',
        'mwai-chatbot',
    );
    foreach ( $handles as $handle ) {
        if ( wp_script_is( $handle, 'registered' ) ) {
            wp_script_add_data( $handle, 'strategy', 'defer' );
        }
    }
}
add_action( 'wp_enqueue_scripts', 'loukas_defer_frontend_scripts', 99 );

/**
 * AI Engine registers 'mwai_chatbot' (which depends on wp-element/React) too late for the
 * wp_enqueue_scripts strategy pass above, so React was being deferred while the chatbot was not.
 * This filter runs at print time, when the handle definitely exists, and defers it too.
 * Deferred scripts execute in document order, so React still runs first. Added 2026-08-30.
 */
function loukas_defer_late_scripts( $tag, $handle ) {
    $late = array( 'mwai_chatbot', 'mwai_highlight' );
    if ( ! in_array( $handle, $late, true ) ) {
        return $tag;
    }
    if ( strpos( $tag, ' defer' ) !== false || strpos( $tag, ' async' ) !== false ) {
        return $tag;
    }
    return str_replace( '<script ', '<script defer ', $tag );
}
add_filter( 'script_loader_tag', 'loukas_defer_late_scripts', 10, 2 );
