<?php get_header(); ?>

<!-- Hero -->
<section id="hero">
  <canvas id="bg-canvas"></canvas>
  <div class="hero-content">
    <div class="eyebrow">Park Ridge, IL &mdash; Accepting New Patients</div>
    <h1 class="hero-h1">Your Family Dentist<br>in <em>Park Ridge</em></h1>
    <p class="hero-desc">Two generations of clinical excellence. Dr. Thanasi Loukas and Dr. Maria Loukas deliver implants, Invisalign, veneers, and complete family care with a gentle, modern touch.</p>
    <div class="hero-ctas">
      <a href="tel:<?php echo loukas_phone_raw(); ?>" class="btn btn-primary">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        Call <?php echo loukas_phone(); ?>
      </a>
      <a href="<?php echo esc_url(get_option('loukas_appointment_url', 'https://www.mogo.com/Registration/Appointment/Index')); ?>" class="btn btn-outline" target="_blank" rel="noopener">Book Appointment</a>
    </div>
    <div class="stats-row">
      <div class="stat"><div class="stat-num">40+</div><div class="stat-label">Years</div></div>
      <div class="stat"><div class="stat-num">5 &#9733;</div><div class="stat-label">Rating</div></div>
      <div class="stat"><div class="stat-num">1,000+</div><div class="stat-label">Smiles</div></div>
    </div>
  </div>
  <div class="scroll-hint"><span></span></div>
  <div class="hero-fade"></div>
</section>

<!-- Services -->
<section class="hp-section">
  <div class="hp-container">
    <p class="hp-eyebrow">What We Do</p>
    <h2 class="hp-h2">Our Services</h2>
    <p class="hp-subtitle">From implants to Invisalign, veneers to Botox &mdash; comprehensive dentistry and facial aesthetics under one roof.</p>
    <div class="hp-grid6">
      <a href="/invisalign/" class="hp-service-tile">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/loukas-instagram-invisalign-clear-aligners.webp" alt="Invisalign" width="400" height="267" loading="lazy">
        <span class="tile-label">Invisalign</span>
      </a>
      <a href="/dental-implants/" class="hp-service-tile">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/before-after-dental-implants_ffab8b60.jpg" alt="Dental Implants" width="400" height="267" loading="lazy">
        <span class="tile-label">Dental Implants</span>
      </a>
      <a href="/porcelain-veneers/" class="hp-service-tile">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/loukas-homepage-veneers-img3377-approved.webp" alt="Porcelain Veneers" width="400" height="267" loading="lazy">
        <span class="tile-label">Porcelain Veneers</span>
      </a>
      <a href="/botox-dysport/" class="hp-service-tile">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/loukas-homepage-botox-dr-loukas-clinical.webp" alt="Botox and Dysport" width="400" height="267" loading="lazy">
        <span class="tile-label">Botox &amp; Dysport</span>
      </a>
      <a href="/dental-crowns/" class="hp-service-tile">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/implant-crowns-before-and-after_e886eb1e.jpg" alt="Dental Crowns" width="400" height="267" loading="lazy">
        <span class="tile-label">Dental Crowns</span>
      </a>
      <a href="/lip-filler/" class="hp-service-tile">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/park-ridge-lip-filler-juvederm-result-2.jpg" alt="Lip Fillers" width="400" height="267" loading="lazy">
        <span class="tile-label">Lip Fillers</span>
      </a>
    </div>
  </div>
</section>

<!-- About -->
<section class="hp-section hp-section-alt">
  <div class="hp-container">
    <div class="hp-grid2">
      <div>
        <p class="hp-eyebrow" style="text-align:left">About Our Practice</p>
        <h2 class="hp-h2" style="text-align:left">The Loukas Dentistry Difference</h2>
        <p class="hp-body-text">When you visit our Park Ridge dental practice, you can expect a complete range of general dentistry treatments in a comfortable setting. We are among the best Chicago dentists and use the latest dental equipment and technology.</p>
        <p class="hp-body-text">Both Dr. Thanasi Loukas and Dr. Maria Loukas have received extensive hands-on training in a wide variety of dental services including placing and restoring dental implants, children&rsquo;s dentistry, Invisalign clear orthodontics, and periodontal care.</p>
        <p class="hp-body-text" style="margin-bottom:24px">We also pride ourselves on using the latest technology &mdash; from digital x-rays to intraoral cameras &mdash; to help provide accurate diagnoses and precision treatment.</p>
        <a href="/about-us/" class="hp-btn hp-btn-teal">Learn More About Us</a>
      </div>
      <div>
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/loukas-dentistry-office-lobby-park-ridge-il.jpg" alt="Loukas Dentistry Office in Park Ridge" class="hp-about-img" width="600" height="400" loading="lazy">
      </div>
    </div>
  </div>
</section>

<!-- Before & After -->
<section class="hp-section hp-section-gray">
  <div class="hp-container">
    <p class="hp-eyebrow">Real Results</p>
    <h2 class="hp-h2">Before &amp; After Results</h2>
    <p class="hp-subtitle">Real patients, real results. See what advanced dentistry can do for your smile.</p>
    <div class="hp-grid3">
      <div class="hp-card">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/invisalign-before-and-after_ada091d8.jpg" alt="Invisalign Before and After" class="hp-card-img" width="400" height="300" loading="lazy">
        <div class="hp-card-body">
          <h3 class="hp-card-title">Invisalign Result</h3>
          <p class="hp-card-desc">Clear aligner orthodontic treatment</p>
        </div>
      </div>
      <div class="hp-card">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/dental-implants-before-after-loukas-dentistry-park-ridge.jpg" alt="Dental Implants Before and After" class="hp-card-img" width="400" height="300" loading="lazy">
        <div class="hp-card-body">
          <h3 class="hp-card-title">Dental Implant</h3>
          <p class="hp-card-desc">Permanent tooth replacement</p>
        </div>
      </div>
      <div class="hp-card">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/after_veneers-scaled.jpg" alt="Porcelain Veneers Result" class="hp-card-img" width="400" height="300" loading="lazy">
        <div class="hp-card-body">
          <h3 class="hp-card-title">Porcelain Veneers</h3>
          <p class="hp-card-desc">Custom smile makeover</p>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Team -->
<section class="hp-section">
  <div class="hp-container">
    <p class="hp-eyebrow">Our Providers</p>
    <h2 class="hp-h2">Meet Our Team</h2>
    <div class="hp-team-group">
      <img src="https://www.drloukas.com/wp-content/uploads/2026/06/loukas-dentistry-team-dr-thanasi-dr-maria-elena-park-ridge.jpg" alt="Loukas Dentistry Team" width="1200" height="500" loading="lazy">
    </div>
    <div class="hp-grid3">
      <div class="hp-card hp-team-card">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/dr-thanasi-loukas-dmd-202606.jpg" alt="Dr. Thanasi Loukas" class="hp-team-photo" width="120" height="120" loading="lazy">
        <h3 class="hp-card-title">Dr. Thanasi Loukas, DMD</h3>
        <p class="hp-team-role">DMD &mdash; General &amp; Cosmetic Dentist</p>
        <p class="hp-card-desc">Specializing in dental implants, cosmetic dentistry, and facial aesthetics with 20+ years of experience.</p>
      </div>
      <div class="hp-card hp-team-card">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/dr-maria-loukas-dds-professional-portrait-20260609011840.jpg" alt="Dr. Maria Loukas" class="hp-team-photo" width="120" height="120" loading="lazy">
        <h3 class="hp-card-title">Dr. Maria Loukas, DDS</h3>
        <p class="hp-team-role">Co-Founder &middot; Est. 1981 &mdash; General &amp; Family Dentistry</p>
        <p class="hp-card-desc">Gentle, comprehensive dental care for patients of all ages.</p>
      </div>
      <div class="hp-card hp-team-card">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/elena-bogis-rdh-202606.jpg" alt="Elena Boggess" class="hp-team-photo" width="120" height="120" loading="lazy">
        <h3 class="hp-card-title">Elena Boggess, RDH</h3>
        <p class="hp-team-role">Dental Hygienist</p>
        <p class="hp-card-desc">Thorough cleanings and personalized oral health education.</p>
      </div>
    </div>
  </div>
</section>

<!-- Testimonials -->
<section class="hp-section hp-section-gray">
  <div class="hp-container">
    <p class="hp-eyebrow">Patient Reviews</p>
    <h2 class="hp-h2">What Our Patients Say</h2>
    <div class="hp-grid3" style="margin-top:40px">
      <div class="hp-card hp-testimonial">
        <div class="hp-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="hp-testimonial-text">&ldquo;Dr. Loukas and his team are amazing. I needed dental implants and was nervous, but they made me feel at ease. The results are incredible!&rdquo;</p>
        <p class="hp-testimonial-name">Michael R.</p>
      </div>
      <div class="hp-card hp-testimonial">
        <div class="hp-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="hp-testimonial-text">&ldquo;I got Invisalign here and the iTero scanner made it so easy &mdash; no goopy impressions! My teeth are already straighter. Friendly and professional.&rdquo;</p>
        <p class="hp-testimonial-name">Sarah K.</p>
      </div>
      <div class="hp-card hp-testimonial">
        <div class="hp-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="hp-testimonial-text">&ldquo;I got Botox and lip fillers and couldn&rsquo;t be happier. Dr. Loukas has a great eye for aesthetics. The office is beautiful. Highly recommend!&rdquo;</p>
        <p class="hp-testimonial-name">Jennifer M.</p>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="hp-section">
  <div class="hp-container" style="max-width:800px">
    <p class="hp-eyebrow">Common Questions</p>
    <h2 class="hp-h2">Frequently Asked Questions</h2>
    <div class="hp-faq-list">
      <div class="hp-faq-item">
        <button class="hp-faq-q" aria-expanded="false">What dental services do you offer?<span class="hp-faq-icon">+</span></button>
        <div class="hp-faq-a" role="region"><p>We offer dental implants, Invisalign, porcelain veneers, teeth whitening, crowns, bridges, root canals, cleanings, Botox, Dysport, lip fillers, and Kybella.</p></div>
      </div>
      <div class="hp-faq-item">
        <button class="hp-faq-q" aria-expanded="false">Do you accept dental insurance?<span class="hp-faq-icon">+</span></button>
        <div class="hp-faq-a" role="region"><p>Yes, we accept most major dental insurance plans. We also offer flexible payment options and CareCredit financing.</p></div>
      </div>
      <div class="hp-faq-item">
        <button class="hp-faq-q" aria-expanded="false">How do I schedule an appointment?<span class="hp-faq-icon">+</span></button>
        <div class="hp-faq-a" role="region"><p>Call <?php echo loukas_phone(); ?> or visit our contact page to submit a request online.</p></div>
      </div>
      <div class="hp-faq-item">
        <button class="hp-faq-q" aria-expanded="false">What are your office hours?<span class="hp-faq-icon">+</span></button>
        <div class="hp-faq-a" role="region"><p>Monday 9&ndash;6, Tuesday 10&ndash;7:30, Wednesday Closed, Thursday 10&ndash;7:30, Friday 9&ndash;2, Saturday 9&ndash;3.</p></div>
      </div>
      <div class="hp-faq-item">
        <button class="hp-faq-q" aria-expanded="false">Do you offer emergency dental care?<span class="hp-faq-icon">+</span></button>
        <div class="hp-faq-a" role="region"><p>Yes, we accommodate same-day emergencies. Call <?php echo loukas_phone(); ?> immediately for urgent dental needs.</p></div>
      </div>
      <div class="hp-faq-item">
        <button class="hp-faq-q" aria-expanded="false">What is Invisalign?<span class="hp-faq-icon">+</span></button>
        <div class="hp-faq-a" role="region"><p>Invisalign uses custom clear aligners to straighten teeth, typically in 6&ndash;18 months. We use the iTero digital scanner for precise planning.</p></div>
      </div>
      <div class="hp-faq-item">
        <button class="hp-faq-q" aria-expanded="false">Are dental implants right for me?<span class="hp-faq-icon">+</span></button>
        <div class="hp-faq-a" role="region"><p>Most healthy adults are candidates. Dr. Loukas uses CBCT 3D imaging to evaluate bone structure and create a personalized plan.</p></div>
      </div>
      <div class="hp-faq-item">
        <button class="hp-faq-q" aria-expanded="false">Do you offer cosmetic dentistry?<span class="hp-faq-icon">+</span></button>
        <div class="hp-faq-a" role="region"><p>Yes &mdash; veneers, whitening, bonding, smile makeovers, Botox, lip fillers, and more.</p></div>
      </div>
    </div>
  </div>
</section>

<!-- Contact -->
<section class="hp-section hp-section-dark">
  <div class="hp-container">
    <div class="hp-grid2">
      <div>
        <h2 class="hp-h2" style="text-align:left;color:#fff">Contact Us</h2>
        <p style="color:#fff;font-size:18px;font-weight:700;margin:0 0 4px">Loukas Dentistry</p>
        <p class="hp-contact-address">714 W Higgins Rd<br>Park Ridge, IL 60068<br><a href="/virtual-tour/">&#128506; Take a Virtual Office Tour &rarr;</a></p>
        <p style="margin:0 0 24px"><a href="tel:<?php echo loukas_phone_raw(); ?>" class="hp-contact-phone"><?php echo loukas_phone(); ?></a></p>
        <table class="hp-contact-hours">
          <tr><td>Monday</td><td>9 AM &ndash; 6 PM</td></tr>
          <tr><td>Tuesday</td><td>10 AM &ndash; 7:30 PM</td></tr>
          <tr><td>Wednesday</td><td class="closed">Closed</td></tr>
          <tr><td>Thursday</td><td>10 AM &ndash; 7:30 PM</td></tr>
          <tr><td>Friday</td><td>9 AM &ndash; 2 PM</td></tr>
          <tr><td>Saturday</td><td>9 AM &ndash; 3 PM</td></tr>
        </table>
      </div>
      <div style="text-align:center">
        <h3 style="font-family:var(--ff-heading);font-size:24px;color:#fff;margin:0 0 16px">Request an Appointment</h3>
        <p class="hp-contact-sub">Call us at <a href="tel:<?php echo loukas_phone_raw(); ?>"><?php echo loukas_phone(); ?></a> or visit us to schedule your appointment today.</p>
        <div class="hp-contact-btns">
          <a href="<?php echo esc_url(get_option('loukas_appointment_url', 'https://www.mogo.com/Registration/Appointment/Index')); ?>" class="hp-btn hp-btn-teal" target="_blank" rel="noopener">Book Online</a>
          <a href="https://maps.google.com/?q=714+W+Higgins+Rd+Park+Ridge+IL+60068" target="_blank" rel="noopener" class="hp-btn hp-btn-outline">Get Directions</a>
        </div>
        <div class="hp-map-embed">
          <iframe src="https://www.google.com/maps/embed?pb=!1m18!1m12!1m3!1d2963.5!2d-87.8360!3d41.9862!2m3!1f0!2f0!3f0!3m2!1i1024!2i768!4f13.1!3m3!1m2!1s0x880fc98d1ff45fb5%3A0x1a10f217a7aa0af2!2sLoukas%20General%20Dentistry!5e0!3m2!1sen!2sus!4v1" width="100%" height="250" style="border:0;border-radius:8px;margin-top:24px" allowfullscreen="" loading="lazy" referrerpolicy="no-referrer-when-downgrade" title="Loukas Dentistry on Google Maps"></iframe>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Communities -->
<section class="hp-communities">
  <div class="hp-container">
    <h3>Proudly Serving Park Ridge &amp; Surrounding Communities</h3>
    <p>Park Ridge &bull; Chicago &bull; Niles &bull; Des Plaines &bull; Norridge &bull; Harwood Heights &bull; Edison Park &bull; Norwood Park</p>
  </div>
</section>

<!-- Mobile Bottom Nav -->
<div id="lk-mobile-nav" role="navigation" aria-label="Quick actions">
  <a href="tel:<?php echo loukas_phone_raw(); ?>" class="lk-nav-call" aria-label="Call us">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
    Call Us
  </a>
  <a href="<?php echo esc_url(get_option('loukas_appointment_url', 'https://www.mogo.com/Registration/Appointment/Index')); ?>" aria-label="Book appointment" target="_blank" rel="noopener">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="4" width="18" height="18" rx="2" ry="2"/><line x1="16" y1="2" x2="16" y2="6"/><line x1="8" y1="2" x2="8" y2="6"/><line x1="3" y1="10" x2="21" y2="10"/></svg>
    Book
  </a>
  <a href="/smile-gallery/" aria-label="View our work">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><rect x="3" y="3" width="18" height="18" rx="2" ry="2"/><circle cx="8.5" cy="8.5" r="1.5"/><polyline points="21 15 16 10 5 21"/></svg>
    Our Work
  </a>
  <a href="https://maps.google.com/?q=714+W+Higgins+Rd+Park+Ridge+IL+60068" target="_blank" rel="noopener" aria-label="Get directions">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><polygon points="3 11 22 2 13 21 11 13 3 11"/></svg>
    Directions
  </a>
</div>

<!-- Schema JSON-LD -->
<script type="application/ld+json">
{"@context":"https://schema.org","@graph":[{"@type":"Dentist","@id":"https://www.drloukas.com/#localbusiness","name":"Loukas Dentistry of Park Ridge","url":"https://www.drloukas.com/","image":"https://www.drloukas.com/wp-content/uploads/2026/05/loukas_logo_master_transparent.png","logo":"https://www.drloukas.com/wp-content/uploads/2026/05/loukas_logo_master_transparent.png","address":{"@type":"PostalAddress","streetAddress":"714 W Higgins Rd","postalCode":"60068","addressLocality":"Park Ridge","addressRegion":"Illinois","addressCountry":"US"},"geo":{"@type":"GeoCoordinates","latitude":41.9861914,"longitude":-87.8338504},"email":"loukasgendentistry@gmail.com","telephone":"+18476961919","priceRange":"$$","currenciesAccepted":"USD","paymentAccepted":"Cash, Credit Cards, CareCredit, Venmo","areaServed":"Park Ridge, Chicago, Niles, Des Plaines, Norridge, Harwood Heights, Edison Park, Norwood Park, IL","aggregateRating":{"@type":"AggregateRating","ratingValue":"5","reviewCount":"83","bestRating":"5","worstRating":"1"},"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday"],"opens":"09:00","closes":"18:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Tuesday"],"opens":"10:00","closes":"19:30"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Thursday"],"opens":"10:00","closes":"19:30"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Friday"],"opens":"09:00","closes":"14:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Saturday"],"opens":"09:00","closes":"15:00"}],"sameAs":["https://www.facebook.com/LoukasDentistry/","https://www.instagram.com/loukasdentistry/"]},{"@type":"Organization","@id":"https://www.drloukas.com/#organization","name":"Loukas Dentistry of Park Ridge","url":"https://www.drloukas.com/","foundingDate":"1981-06-07","numberOfEmployees":{"@type":"QuantitativeValue","value":6},"logo":{"@type":"ImageObject","url":"https://www.drloukas.com/wp-content/uploads/2026/05/loukas_logo_master_transparent.png","width":1000,"height":746},"sameAs":["https://www.facebook.com/LoukasDentistry/","https://www.instagram.com/loukasdentistry/"]},{"@type":"WebSite","@id":"https://www.drloukas.com/#website","url":"https://www.drloukas.com/","name":"Loukas Dentistry of Park Ridge","description":"Family and implant dentistry in Park Ridge, IL","publisher":{"@id":"https://www.drloukas.com/#organization"}},{"@type":"VideoObject","name":"Watch a Botox Treatment at Loukas Dentistry Park Ridge","description":"Watch Dr. Thanasi Loukas perform a live Botox treatment session at Loukas Dentistry of Park Ridge, IL.","thumbnailUrl":"https://img.youtube.com/vi/8nwlO4GGDyw/maxresdefault.jpg","uploadDate":"2026-06-15","duration":"PT3M","contentUrl":"https://www.youtube.com/watch?v=8nwlO4GGDyw","embedUrl":"https://www.youtube.com/embed/8nwlO4GGDyw","publisher":{"@type":"Organization","name":"Loukas Dentistry of Park Ridge","logo":{"@type":"ImageObject","url":"https://www.drloukas.com/wp-content/uploads/2026/05/loukas_logo_master_transparent.png"}}},{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What dental services do you offer?","acceptedAnswer":{"@type":"Answer","text":"We offer dental implants, Invisalign, porcelain veneers, teeth whitening, crowns, bridges, root canals, cleanings, Botox, Dysport, lip fillers, and Kybella."}},{"@type":"Question","name":"Do you accept dental insurance?","acceptedAnswer":{"@type":"Answer","text":"Yes, we accept most major dental insurance plans. We also offer flexible payment options and CareCredit financing."}},{"@type":"Question","name":"How do I schedule an appointment?","acceptedAnswer":{"@type":"Answer","text":"Call (847) 696-1919 or visit our contact page to submit a request online."}},{"@type":"Question","name":"What are your office hours?","acceptedAnswer":{"@type":"Answer","text":"Monday 9-6, Tuesday 10-7:30, Wednesday Closed, Thursday 10-7:30, Friday 9-2, Saturday 9-3."}},{"@type":"Question","name":"Do you offer emergency dental care?","acceptedAnswer":{"@type":"Answer","text":"Yes, we accommodate same-day emergencies. Call (847) 696-1919 immediately for urgent dental needs."}},{"@type":"Question","name":"What is Invisalign?","acceptedAnswer":{"@type":"Answer","text":"Invisalign uses custom clear aligners to straighten teeth, typically in 6-18 months. We use the iTero digital scanner for precise planning."}},{"@type":"Question","name":"Are dental implants right for me?","acceptedAnswer":{"@type":"Answer","text":"Most healthy adults are candidates. Dr. Loukas uses CBCT 3D imaging to evaluate bone structure and create a personalized plan."}},{"@type":"Question","name":"Do you offer cosmetic dentistry?","acceptedAnswer":{"@type":"Answer","text":"Yes - veneers, whitening, bonding, smile makeovers, Botox, lip fillers, and more."}}]}]}
</script>

<?php get_footer(); ?>
