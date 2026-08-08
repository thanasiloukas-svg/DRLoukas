<?php get_header(); ?>
<main class="lk-main">
  <div class="lk-container">
    <?php if (function_exists('aioseo_breadcrumbs')) { aioseo_breadcrumbs(); } ?>
    <header class="lk-archive-header">
      <h1 class="lk-page-title"><?php the_archive_title(); ?></h1>
      <?php the_archive_description('<p class="lk-archive-desc">','</p>'); ?>
    </header>
    <?php if (have_posts()): ?>
      <div class="lk-post-grid">
        <?php while (have_posts()): the_post(); ?>
          <article class="lk-post-card hp-card">
            <?php if (has_post_thumbnail()): ?>
              <a href="<?php the_permalink(); ?>" class="lk-post-card-thumb">
                <?php the_post_thumbnail('medium_large'); ?>
              </a>
            <?php endif; ?>
            <div class="lk-post-card-body">
              <h2 class="lk-post-card-title"><a href="<?php the_permalink(); ?>"><?php the_title(); ?></a></h2>
              <time class="lk-post-card-date" datetime="<?php echo get_the_date('c'); ?>"><?php echo get_the_date(); ?></time>
              <p class="lk-post-card-excerpt"><?php echo wp_trim_words(get_the_excerpt(), 20); ?></p>
              <a href="<?php the_permalink(); ?>" class="lk-read-more">Read More &rarr;</a>
            </div>
          </article>
        <?php endwhile; ?>
      </div>
      <div class="lk-pagination">
        <?php the_posts_pagination(['mid_size' => 2, 'prev_text' => '&larr;', 'next_text' => '&rarr;']); ?>
      </div>
    <?php else: ?>
      <p>No posts found.</p>
    <?php endif; ?>
  </div>
</main>
<?php get_footer(); ?>
