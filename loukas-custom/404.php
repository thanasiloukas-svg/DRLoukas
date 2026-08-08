<?php get_header(); ?>
<main class="lk-main lk-404">
  <div class="lk-container" style="text-align:center;min-height:50vh;display:flex;flex-direction:column;align-items:center;justify-content:center">
    <h1 class="hp-h2" style="font-size:48px;margin-bottom:16px">404</h1>
    <p class="hp-subtitle" style="margin-bottom:32px">Sorry, the page you're looking for doesn't exist or has been moved.</p>
    <a href="<?php echo esc_url(home_url('/')); ?>" class="hp-btn hp-btn-teal">Back to Homepage</a>
  </div>
</main>
<?php get_footer(); ?>
