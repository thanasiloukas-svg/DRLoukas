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
      <picture><source srcset="https://www.drloukas.com/wp-content/uploads/2026/08/loukas-logo-header.webp" type="image/webp"><img src="https://www.drloukas.com/wp-content/uploads/2026/08/loukas-logo-header.png" alt="<?php bloginfo('name'); ?>" width="161" height="120" loading="eager" fetchpriority="high"></picture>
    </a>

    <nav class="header-nav" id="header-nav">
      <?php
      wp_nav_menu([
        'theme_location' => 'primary',
        'container'      => false,
        'menu_class'     => 'nav-list',
        'fallback_cb'    => 'loukas_fallback_menu',
        'depth'          => 2,
      ]);
      ?>
    </nav>

    <div class="header-actions">
      <a href="https://maps.google.com/?q=714+W+Higgins+Rd+Park+Ridge+IL+60068" target="_blank" rel="noopener" class="header-cta header-cta-dir">Directions</a>
      <a href="/contact-us/" class="header-cta">Appointment</a>
    </div>

    <button class="mobile-toggle" id="mobile-toggle" aria-label="Toggle menu" aria-expanded="false">
      <span></span><span></span><span></span>
    </button>
  </div>
</header>
