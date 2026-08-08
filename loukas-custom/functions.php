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
    echo '<li><a href="/invisalign/">Invisalign</a></li>';
    echo '<li><a href="/porcelain-veneers/">Porcelain Veneers</a></li>';
    echo '<li><a href="/teeth-whitening/">Teeth Whitening</a></li>';
    echo '<li><a href="/dental-crowns/">Dental Crowns</a></li>';
    echo '<li><a href="/root-canal/">Root Canals</a></li>';
    echo '<li><a href="/sedation-dentistry/">Sedation Dentistry</a></li>';
    echo '<li><a href="/sleep-apnea-snoring-treatment/">Sleep Apnea</a></li>';
    echo '<li><a href="/permanent-gold-teeth/">Gold Crowns</a></li>';
    echo '</ul></li>';
    echo '<li class="menu-item-has-children"><a href="/cosmetic-dentistry/">Cosmetic &amp; Med Spa</a>';
    echo '<ul class="sub-menu">';
    echo '<li><a href="/botox-dysport/">Botox &amp; Dysport</a></li>';
    echo '<li><a href="/lip-filler/">Lip Fillers</a></li>';
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
