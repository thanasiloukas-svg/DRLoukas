<!DOCTYPE html>
<html <?php language_attributes(); ?>>
<head>
<meta charset="<?php bloginfo('charset'); ?>">
<meta name="viewport" content="width=device-width, initial-scale=1">
<?php wp_head(); ?>
</head>
<body <?php body_class(); ?>>
<?php wp_body_open(); ?>

<header class="site-header" id="site-header">
  <div class="header-inner">
    <a href="<?php echo esc_url(home_url('/')); ?>" class="header-logo">
      <img src="https://www.drloukas.com/wp-content/uploads/2024/10/cropped-loukas-general-dentistry-park-ridge-logo-2021.png" alt="<?php bloginfo('name'); ?>" width="200" height="48">
    </a>

    <nav class="header-nav" id="header-nav">
      <?php
      wp_nav_menu([
        'theme_location' => 'primary',
        'container'      => false,
        'menu_class'     => 'nav-list',
        'fallback_cb'    => 'loukas_fallback_menu',
        'depth'          => 1,
      ]);
      ?>
    </nav>

    <div class="header-actions">
      <a href="tel:<?php echo loukas_phone_raw(); ?>" class="header-phone">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        <span><?php echo loukas_phone(); ?></span>
      </a>
      <a href="/appointments/" class="header-cta">Book Appointment</a>
    </div>

    <button class="mobile-toggle" id="mobile-toggle" aria-label="Toggle menu">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>

<?php
function loukas_fallback_menu() {
    echo '<ul class="nav-list">';
    echo '<li><a href="/about-us/">About</a></li>';
    echo '<li><a href="/dental-implants/">Implants</a></li>';
    echo '<li><a href="/invisalign/">Invisalign</a></li>';
    echo '<li><a href="/porcelain-veneers/">Veneers</a></li>';
    echo '<li><a href="/botox-dysport/">Botox</a></li>';
    echo '<li><a href="/contact/">Contact</a></li>';
    echo '</ul>';
}
?>
