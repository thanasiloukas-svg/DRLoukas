<?php
defined('ABSPATH') || exit;

function loukas_setup() {
    add_theme_support('title-tag');
    add_theme_support('post-thumbnails');
    add_theme_support('html5', ['search-form','comment-form','comment-list','gallery','caption','style','script']);
    register_nav_menus(['primary' => 'Primary Menu']);
}
add_action('after_setup_theme', 'loukas_setup');

function loukas_enqueue() {
    $v = wp_get_theme()->get('Version');
    wp_enqueue_style('google-fonts',
        'https://fonts.googleapis.com/css2?family=Playfair+Display:wght@400;600;700&family=Source+Sans+3:wght@300;400;600;700&display=swap',
        [], null);
    wp_enqueue_style('loukas-main', get_template_directory_uri() . '/css/main.css', [], $v);

    if (is_front_page()) {
        wp_enqueue_script('loukas-hero', get_template_directory_uri() . '/js/hero-animation.js', [], $v, true);
    }
    wp_enqueue_script('loukas-main', get_template_directory_uri() . '/js/main.js', [], $v, true);
}
add_action('wp_enqueue_scripts', 'loukas_enqueue');

function loukas_phone() { return '(847) 696-1919'; }
function loukas_phone_raw() { return '8476961919'; }
