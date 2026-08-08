<?php get_header(); ?>
<main class="hp-section">
  <div class="hp-container">
    <?php if (have_posts()): while (have_posts()): the_post(); ?>
      <article>
        <h1 class="hp-h2" style="text-align:left"><?php the_title(); ?></h1>
        <div class="page-content"><?php the_content(); ?></div>
      </article>
    <?php endwhile; endif; ?>
  </div>
</main>
<?php get_footer(); ?>
