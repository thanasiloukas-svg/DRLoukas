<?php get_header(); ?>
<main class="lk-main">
  <div class="lk-container">
    <?php if (have_posts()): while (have_posts()): the_post(); ?>
      <article class="lk-article">
        <h1 class="lk-page-title"><?php the_title(); ?></h1>
        <div class="lk-content"><?php the_content(); ?></div>
      </article>
    <?php endwhile; endif; ?>
  </div>
</main>
<?php get_footer(); ?>
