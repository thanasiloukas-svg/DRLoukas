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
      <img src="https://www.drloukas.com/wp-content/uploads/2026/05/loukas_logo_master_transparent.png" alt="<?php bloginfo('name'); ?>" width="200" height="48" loading="eager">
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
