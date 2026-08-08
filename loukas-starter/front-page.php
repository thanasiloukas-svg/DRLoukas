<?php get_header(); ?>

<!-- Hero -->
<section id="hero">
  <canvas id="bg-canvas"></canvas>
  <div class="hero-content">
    <div class="eyebrow">Park Ridge, IL &mdash; Accepting New Patients</div>
    <h1 class="hero-h1">Your Family Dentist<br>in <em>Park Ridge</em></h1>
    <p class="hero-desc">Two generations of clinical excellence. Dr. Thanasi Loukas and Dr. Maria Loukas deliver implants, Invisalign, veneers, and complete family care with a gentle, modern touch.</p>
    <div class="hero-ctas">
      <a href="tel:<?php echo loukas_phone_raw(); ?>" class="hp-btn-pill primary">
        <svg width="16" height="16" viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.5" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
        Call <?php echo loukas_phone(); ?>
      </a>
      <a href="/appointments/" class="hp-btn-pill outline">Book Appointment</a>
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
      <a href="/dental-implants/" class="hp-service-tile">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/loukas-homepage-dental-implants.jpg" alt="Dental Implants" loading="lazy">
        <span class="tile-label">Dental Implants</span>
      </a>
      <a href="/invisalign/" class="hp-service-tile">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/loukas-instagram-invisalign-clear-aligners.webp" alt="Invisalign" loading="lazy">
        <span class="tile-label">Invisalign</span>
      </a>
      <a href="/porcelain-veneers/" class="hp-service-tile">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/loukas-homepage-veneers-img3377-approved.webp" alt="Porcelain Veneers" loading="lazy">
        <span class="tile-label">Porcelain Veneers</span>
      </a>
      <a href="/botox-dysport/" class="hp-service-tile">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/loukas-homepage-botox-dr-loukas-clinical.webp" alt="Botox and Dysport" loading="lazy">
        <span class="tile-label">Botox &amp; Dysport</span>
      </a>
      <a href="/dental-crowns/" class="hp-service-tile">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/loukas-instagram-porcelain-crowns-result.webp" alt="Dental Crowns" loading="lazy">
        <span class="tile-label">Dental Crowns</span>
      </a>
      <a href="/lip-filler/" class="hp-service-tile">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/park-ridge-lip-filler-juvederm-result-2.jpg" alt="Lip Fillers" loading="lazy">
        <span class="tile-label">Lip Fillers</span>
      </a>
    </div>
  </div>
</section>

<!-- About -->
<section class="hp-section" style="background:var(--light-bg)">
  <div class="hp-container">
    <div class="hp-grid2">
      <div>
        <p class="hp-eyebrow" style="text-align:left">About Our Practice</p>
        <h2 class="hp-h2" style="text-align:left">The Loukas Dentistry Difference</h2>
        <p style="color:var(--text);font-size:16px;line-height:1.7;margin-bottom:16px">When you visit our Park Ridge dental practice, you can expect a complete range of general dentistry treatments in a comfortable setting. We are among the best Chicago dentists and use the latest dental equipment and technology.</p>
        <p style="color:var(--text);font-size:16px;line-height:1.7;margin-bottom:16px">Both Dr. Thanasi Loukas and Dr. Maria Loukas have received extensive hands-on training in a wide variety of dental services including placing and restoring dental implants, children&rsquo;s dentistry, Invisalign clear orthodontics, and periodontal care.</p>
        <p style="color:var(--text);font-size:16px;line-height:1.7;margin-bottom:24px">We also pride ourselves on using the latest technology &mdash; from digital x-rays to intraoral cameras &mdash; to help provide accurate diagnoses and precision treatment.</p>
        <a href="/about-us/" class="hp-btn hp-btn-teal">Learn More About Us</a>
      </div>
      <div>
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/loukas-dentistry-office-lobby-park-ridge-il.jpg" alt="Loukas Dentistry Office in Park Ridge" style="width:100%;border-radius:12px;box-shadow:0 8px 32px rgba(6,32,45,.12)" loading="lazy">
      </div>
    </div>
  </div>
</section>

<!-- Before & After -->
<section class="hp-section" style="background:#F8F9FA">
  <div class="hp-container">
    <p class="hp-eyebrow">Real Results</p>
    <h2 class="hp-h2">Before &amp; After Results</h2>
    <p class="hp-subtitle">Real patients, real results. See what advanced dentistry can do for your smile.</p>
    <div class="hp-grid3">
      <div class="hp-card">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/invisalign-before-and-after_ada091d8.jpg" alt="Invisalign Before and After" style="width:100%;aspect-ratio:4/3;object-fit:cover;display:block" loading="lazy">
        <div style="padding:20px">
          <h3 class="card-title">Invisalign Result</h3>
          <p class="card-desc">Clear aligner orthodontic treatment</p>
        </div>
      </div>
      <div class="hp-card">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/dental-implants-before-after-loukas-dentistry-park-ridge.jpg" alt="Dental Implants Before and After" style="width:100%;aspect-ratio:4/3;object-fit:cover;display:block" loading="lazy">
        <div style="padding:20px">
          <h3 class="card-title">Dental Implant</h3>
          <p class="card-desc">Permanent tooth replacement</p>
        </div>
      </div>
      <div class="hp-card">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/after_veneers-scaled.jpg" alt="Porcelain Veneers Result" style="width:100%;aspect-ratio:4/3;object-fit:cover;display:block" loading="lazy">
        <div style="padding:20px">
          <h3 class="card-title">Porcelain Veneers</h3>
          <p class="card-desc">Custom smile makeover</p>
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
    <div style="margin-bottom:40px">
      <img src="https://www.drloukas.com/wp-content/uploads/2026/06/loukas-dentistry-team-dr-thanasi-dr-maria-elena-park-ridge.jpg" alt="Loukas Dentistry Team" style="width:100%;border-radius:12px;box-shadow:0 4px 24px rgba(6,32,45,.1)" loading="lazy">
    </div>
    <div class="hp-grid3">
      <div class="hp-card team-card">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/dr-thanasi-loukas-dmd-202606.jpg" alt="Dr. Thanasi Loukas" class="team-photo" loading="lazy">
        <h3 class="card-title">Dr. Thanasi Loukas, DMD</h3>
        <p class="team-role">DMD &mdash; General &amp; Cosmetic Dentist</p>
        <p class="card-desc">Specializing in dental implants, cosmetic dentistry, and facial aesthetics with 20+ years of experience.</p>
      </div>
      <div class="hp-card team-card">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/dr-maria-loukas-dds-professional-portrait-20260609011840.jpg" alt="Dr. Maria Loukas" class="team-photo" loading="lazy">
        <h3 class="card-title">Dr. Maria Loukas, DDS</h3>
        <p class="team-role">Co-Founder &middot; Est. 1981 &mdash; General &amp; Family Dentistry</p>
        <p class="card-desc">Gentle, comprehensive dental care for patients of all ages.</p>
      </div>
      <div class="hp-card team-card">
        <img src="https://www.drloukas.com/wp-content/uploads/2026/06/elena-bogis-rdh-202606.jpg" alt="Elena Boggess" class="team-photo" loading="lazy">
        <h3 class="card-title">Elena Boggess, RDH</h3>
        <p class="team-role">Dental Hygienist</p>
        <p class="card-desc">Thorough cleanings and personalized oral health education.</p>
      </div>
    </div>
  </div>
</section>

<!-- Testimonials -->
<section class="hp-section" style="background:#F8F9FA">
  <div class="hp-container">
    <p class="hp-eyebrow">Patient Reviews</p>
    <h2 class="hp-h2">What Our Patients Say</h2>
    <div class="hp-grid3" style="margin-top:40px">
      <div class="hp-card testimonial-card">
        <div class="hp-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="testimonial-text">&ldquo;Dr. Loukas and his team are amazing. I needed dental implants and was nervous, but they made me feel at ease. The results are incredible!&rdquo;</p>
        <p class="testimonial-name">Michael R.</p>
      </div>
      <div class="hp-card testimonial-card">
        <div class="hp-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="testimonial-text">&ldquo;I got Invisalign here and the iTero scanner made it so easy &mdash; no goopy impressions! My teeth are already straighter. Friendly and professional.&rdquo;</p>
        <p class="testimonial-name">Sarah K.</p>
      </div>
      <div class="hp-card testimonial-card">
        <div class="hp-stars">&#9733;&#9733;&#9733;&#9733;&#9733;</div>
        <p class="testimonial-text">&ldquo;I got Botox and lip fillers and couldn&rsquo;t be happier. Dr. Loukas has a great eye for aesthetics. The office is beautiful. Highly recommend!&rdquo;</p>
        <p class="testimonial-name">Jennifer M.</p>
      </div>
    </div>
  </div>
</section>

<!-- FAQ -->
<section class="hp-section">
  <div class="hp-container" style="max-width:800px">
    <p class="hp-eyebrow">Common Questions</p>
    <h2 class="hp-h2">Frequently Asked Questions</h2>
    <div style="margin-top:40px">
      <div class="hp-faq-item">
        <button class="hp-faq-q">What dental services do you offer?<span class="hp-faq-icon">+</span></button>
        <div class="hp-faq-a"><p>We offer dental implants, Invisalign, porcelain veneers, teeth whitening, crowns, bridges, root canals, cleanings, Botox, Dysport, lip fillers, and Kybella.</p></div>
      </div>
      <div class="hp-faq-item">
        <button class="hp-faq-q">Do you accept dental insurance?<span class="hp-faq-icon">+</span></button>
        <div class="hp-faq-a"><p>Yes, we accept most major dental insurance plans. We also offer flexible payment options and CareCredit financing.</p></div>
      </div>
      <div class="hp-faq-item">
        <button class="hp-faq-q">How do I schedule an appointment?<span class="hp-faq-icon">+</span></button>
        <div class="hp-faq-a"><p>Call <?php echo loukas_phone(); ?> or visit our contact page to submit a request online.</p></div>
      </div>
      <div class="hp-faq-item">
        <button class="hp-faq-q">What are your office hours?<span class="hp-faq-icon">+</span></button>
        <div class="hp-faq-a"><p>Monday 9&ndash;6, Tuesday 10&ndash;7:30, Wednesday Closed, Thursday 10&ndash;7:30, Friday 9&ndash;2, Saturday 9&ndash;3.</p></div>
      </div>
      <div class="hp-faq-item">
        <button class="hp-faq-q">Do you offer emergency dental care?<span class="hp-faq-icon">+</span></button>
        <div class="hp-faq-a"><p>Yes, we accommodate same-day emergencies. Call <?php echo loukas_phone(); ?> immediately for urgent dental needs.</p></div>
      </div>
      <div class="hp-faq-item">
        <button class="hp-faq-q">What is Invisalign?<span class="hp-faq-icon">+</span></button>
        <div class="hp-faq-a"><p>Invisalign uses custom clear aligners to straighten teeth, typically in 6&ndash;18 months. We use the iTero digital scanner for precise planning.</p></div>
      </div>
      <div class="hp-faq-item">
        <button class="hp-faq-q">Are dental implants right for me?<span class="hp-faq-icon">+</span></button>
        <div class="hp-faq-a"><p>Most healthy adults are candidates. Dr. Loukas uses CBCT 3D imaging to evaluate bone structure and create a personalized plan.</p></div>
      </div>
      <div class="hp-faq-item">
        <button class="hp-faq-q">Do you offer cosmetic dentistry?<span class="hp-faq-icon">+</span></button>
        <div class="hp-faq-a"><p>Yes &mdash; veneers, whitening, bonding, smile makeovers, Botox, lip fillers, and more.</p></div>
      </div>
    </div>
  </div>
</section>

<!-- Contact -->
<section class="hp-section contact-section" style="background:var(--navy)">
  <div class="hp-container">
    <div class="hp-grid2">
      <div>
        <h2 style="font-family:var(--ff-heading);font-size:36px;color:#fff;margin:0 0 24px;line-height:1.3">Contact Us</h2>
        <p style="color:#fff;font-size:18px;font-weight:700;margin:0 0 4px">Loukas Dentistry</p>
        <p style="margin:0 0 16px;line-height:1.6">714 W Higgins Rd<br>Park Ridge, IL 60068<br><a href="/virtual-tour/" style="color:var(--teal);font-weight:700">&#128506; Take a Virtual Office Tour &rarr;</a></p>
        <p style="margin:0 0 24px"><a href="tel:<?php echo loukas_phone_raw(); ?>" style="color:var(--teal);font-size:26px;font-weight:700;text-decoration:none"><?php echo loukas_phone(); ?></a></p>
        <table style="font-size:15px;border-collapse:collapse">
          <tr><td style="padding:4px 24px 4px 0">Monday</td><td>9 AM &ndash; 6 PM</td></tr>
          <tr><td style="padding:4px 24px 4px 0">Tuesday</td><td>10 AM &ndash; 7:30 PM</td></tr>
          <tr><td style="padding:4px 24px 4px 0">Wednesday</td><td style="color:var(--teal)">Closed</td></tr>
          <tr><td style="padding:4px 24px 4px 0">Thursday</td><td>10 AM &ndash; 7:30 PM</td></tr>
          <tr><td style="padding:4px 24px 4px 0">Friday</td><td>9 AM &ndash; 2 PM</td></tr>
          <tr><td style="padding:4px 24px 4px 0">Saturday</td><td>9 AM &ndash; 3 PM</td></tr>
        </table>
      </div>
      <div style="text-align:center">
        <h3 style="font-family:var(--ff-heading);font-size:24px;color:#fff;margin:0 0 16px">Request an Appointment</h3>
        <p style="margin:0 0 24px;line-height:1.6">Call us at <a href="tel:<?php echo loukas_phone_raw(); ?>" style="color:var(--teal);text-decoration:none"><?php echo loukas_phone(); ?></a> or visit us to schedule your appointment today.</p>
        <div>
          <a href="/appointments/" class="hp-btn hp-btn-teal" style="margin:8px">Book Online</a>
          <a href="https://maps.google.com/?q=714+W+Higgins+Rd+Park+Ridge+IL+60068" target="_blank" rel="noopener" class="hp-btn hp-btn-outline" style="margin:8px">Get Directions</a>
        </div>
      </div>
    </div>
  </div>
</section>

<!-- Communities -->
<section style="background:#F8F9FA;padding:40px 20px;text-align:center">
  <div style="max-width:800px;margin:0 auto">
    <h3 style="font-family:var(--ff-heading);font-size:20px;color:var(--navy);margin:0 0 12px">Proudly Serving Park Ridge &amp; Surrounding Communities</h3>
    <p style="color:var(--text-light);font-size:14px;line-height:1.6;margin:0">Park Ridge &bull; Chicago &bull; Niles &bull; Des Plaines &bull; Norridge &bull; Harwood Heights &bull; Edison Park &bull; Norwood Park</p>
  </div>
</section>

<!-- Mobile Bottom Nav -->
<div id="lk-mobile-nav" role="navigation" aria-label="Quick actions">
  <a href="tel:<?php echo loukas_phone_raw(); ?>" class="lk-nav-call" aria-label="Call us">
    <svg viewBox="0 0 24 24" fill="none" stroke="currentColor" stroke-width="2.2" stroke-linecap="round" stroke-linejoin="round"><path d="M22 16.92v3a2 2 0 0 1-2.18 2 19.79 19.79 0 0 1-8.63-3.07 19.5 19.5 0 0 1-6-6 19.79 19.79 0 0 1-3.07-8.67A2 2 0 0 1 4.11 2h3a2 2 0 0 1 2 1.72c.127.96.361 1.903.7 2.81a2 2 0 0 1-.45 2.11L8.09 9.91a16 16 0 0 0 6 6l1.27-1.27a2 2 0 0 1 2.11-.45c.907.339 1.85.573 2.81.7A2 2 0 0 1 22 16.92z"/></svg>
    Call Us
  </a>
  <a href="/contact-us/" aria-label="Book appointment">
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

<!-- Schema: LocalBusiness + FAQ -->
<script type="application/ld+json">
{"@context":"https://schema.org","@graph":[{"@type":"Dentist","@id":"https://www.drloukas.com/#localbusiness","name":"Loukas Dentistry of Park Ridge","url":"https://www.drloukas.com/","image":"https://www.drloukas.com/wp-content/uploads/2026/05/loukas_logo_master_transparent.png","logo":"https://www.drloukas.com/wp-content/uploads/2026/05/loukas_logo_master_transparent.png","address":{"@type":"PostalAddress","streetAddress":"714 W Higgins Rd","postalCode":"60068","addressLocality":"Park Ridge","addressRegion":"Illinois","addressCountry":"US"},"geo":{"@type":"GeoCoordinates","latitude":42.0111,"longitude":-87.8406},"email":"loukasgendentistry@gmail.com","telephone":"+18476961919","priceRange":"$$","currenciesAccepted":"USD","paymentAccepted":"Cash, Credit Cards, CareCredit, Venmo","areaServed":"Park Ridge, Chicago, Niles, Des Plaines, Norridge, Harwood Heights, Edison Park, Norwood Park, IL","aggregateRating":{"@type":"AggregateRating","ratingValue":"5","reviewCount":"83","bestRating":"5","worstRating":"1"},"openingHoursSpecification":[{"@type":"OpeningHoursSpecification","dayOfWeek":["Monday"],"opens":"09:00","closes":"18:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Tuesday"],"opens":"10:00","closes":"19:30"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Thursday"],"opens":"10:00","closes":"19:30"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Friday"],"opens":"09:00","closes":"14:00"},{"@type":"OpeningHoursSpecification","dayOfWeek":["Saturday"],"opens":"09:00","closes":"15:00"}],"sameAs":["https://www.facebook.com/LoukasDentistry/","https://www.instagram.com/loukasdentistry/"]},{"@type":"Organization","@id":"https://www.drloukas.com/#organization","name":"Loukas Dentistry of Park Ridge","url":"https://www.drloukas.com/","foundingDate":"1981-06-07","numberOfEmployees":{"@type":"QuantitativeValue","value":6},"logo":{"@type":"ImageObject","url":"https://www.drloukas.com/wp-content/uploads/2026/05/loukas_logo_master_transparent.png","width":1000,"height":746},"sameAs":["https://www.facebook.com/LoukasDentistry/","https://www.instagram.com/loukasdentistry/"]},{"@type":"WebSite","@id":"https://www.drloukas.com/#website","url":"https://www.drloukas.com/","name":"Loukas Dentistry of Park Ridge","description":"Family and implant dentistry in Park Ridge, IL","publisher":{"@id":"https://www.drloukas.com/#organization"}},{"@type":"FAQPage","mainEntity":[{"@type":"Question","name":"What dental services do you offer?","acceptedAnswer":{"@type":"Answer","text":"We offer dental implants, Invisalign, porcelain veneers, teeth whitening, crowns, bridges, root canals, cleanings, Botox, Dysport, lip fillers, and Kybella."}},{"@type":"Question","name":"Do you accept dental insurance?","acceptedAnswer":{"@type":"Answer","text":"Yes, we accept most major dental insurance plans. We also offer flexible payment options and CareCredit financing."}},{"@type":"Question","name":"How do I schedule an appointment?","acceptedAnswer":{"@type":"Answer","text":"Call (847) 696-1919 or visit our contact page to submit a request online."}},{"@type":"Question","name":"What are your office hours?","acceptedAnswer":{"@type":"Answer","text":"Monday 9-6, Tuesday 10-7:30, Wednesday Closed, Thursday 10-7:30, Friday 9-2, Saturday 9-3."}},{"@type":"Question","name":"Do you offer emergency dental care?","acceptedAnswer":{"@type":"Answer","text":"Yes, we accommodate same-day emergencies. Call (847) 696-1919 immediately for urgent dental needs."}},{"@type":"Question","name":"What is Invisalign?","acceptedAnswer":{"@type":"Answer","text":"Invisalign uses custom clear aligners to straighten teeth, typically in 6-18 months. We use the iTero digital scanner for precise planning."}},{"@type":"Question","name":"Are dental implants right for me?","acceptedAnswer":{"@type":"Answer","text":"Most healthy adults are candidates. Dr. Loukas uses CBCT 3D imaging to evaluate bone structure and create a personalized plan."}},{"@type":"Question","name":"Do you offer cosmetic dentistry?","acceptedAnswer":{"@type":"Answer","text":"Yes - veneers, whitening, bonding, smile makeovers, Botox, lip fillers, and more."}}]}]}
</script>

<?php get_footer(); ?>
