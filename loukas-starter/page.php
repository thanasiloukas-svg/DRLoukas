<?php get_header(); ?>
<main class="hp-section" style="padding-top:120px">
  <div class="hp-container">
    <?php if (have_posts()): while (have_posts()): the_post(); ?>
      <article>
        <h1 class="hp-h2" style="text-align:left;margin-bottom:24px"><?php the_title(); ?></h1>
        <div class="page-content" style="color:var(--text);font-size:16px;line-height:1.7"><?php the_content(); ?></div>
      </article>
    <?php endwhile; endif; ?>
  </div>
</main>
<?php get_footer(); ?>
