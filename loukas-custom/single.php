<?php get_header(); ?>
<main class="lk-main">
  <div class="lk-container lk-container-narrow">
    <?php if (function_exists('aioseo_breadcrumbs')) { aioseo_breadcrumbs(); } ?>
    <?php if (have_posts()): while (have_posts()): the_post(); ?>
      <article class="lk-article lk-post">
        <header class="lk-post-header">
          <h1 class="lk-page-title"><?php the_title(); ?></h1>
          <div class="lk-post-meta">
            <time datetime="<?php echo get_the_date('c'); ?>"><?php echo get_the_date(); ?></time>
            <?php if (has_category()): ?>
              <span class="lk-post-cats"><?php the_category(', '); ?></span>
            <?php endif; ?>
          </div>
        </header>
        <?php if (has_post_thumbnail()): ?>
          <div class="lk-post-thumb"><?php the_post_thumbnail('large'); ?></div>
        <?php endif; ?>
        <div class="lk-content"><?php the_content(); ?></div>
      </article>
    <?php endwhile; endif; ?>
  </div>
</main>
<?php get_footer(); ?>
