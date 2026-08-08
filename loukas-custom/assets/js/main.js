(function () {
  var header = document.getElementById('site-header');
  var toggle = document.getElementById('mobile-toggle');

  // Sticky header scroll class
  if (header) {
    window.addEventListener('scroll', function () {
      if (window.scrollY > 50) header.classList.add('scrolled');
      else header.classList.remove('scrolled');
    }, { passive: true });
  }

  // Mobile menu toggle
  if (toggle && header) {
    toggle.addEventListener('click', function () {
      var open = header.classList.toggle('nav-open');
      toggle.setAttribute('aria-expanded', open ? 'true' : 'false');
    });
  }

  // Mobile dropdown toggles
  var parents = document.querySelectorAll('.menu-item-has-children');
  for (var i = 0; i < parents.length; i++) {
    parents[i].querySelector('a').addEventListener('click', function (e) {
      if (window.innerWidth <= 1024) {
        e.preventDefault();
        this.parentElement.classList.toggle('sub-open');
      }
    });
  }

  // FAQ accordion
  var faqButtons = document.querySelectorAll('.hp-faq-q');
  for (var j = 0; j < faqButtons.length; j++) {
    faqButtons[j].addEventListener('click', function () {
      var answer = this.nextElementSibling;
      var icon = this.querySelector('.hp-faq-icon');
      var isOpen = this.getAttribute('aria-expanded') === 'true';
      if (isOpen) {
        answer.style.maxHeight = '0';
        answer.style.paddingBottom = '0';
        if (icon) icon.style.transform = 'rotate(0deg)';
        this.setAttribute('aria-expanded', 'false');
      } else {
        answer.style.maxHeight = answer.scrollHeight + 20 + 'px';
        answer.style.paddingBottom = '20px';
        if (icon) icon.style.transform = 'rotate(45deg)';
        this.setAttribute('aria-expanded', 'true');
      }
    });
  }

  // Scroll reveal
  var sections = document.querySelectorAll('.hp-section');
  if (sections.length && 'IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      for (var k = 0; k < entries.length; k++) {
        if (entries[k].isIntersecting) {
          entries[k].target.classList.add('revealed');
          observer.unobserve(entries[k].target);
        }
      }
    }, { threshold: 0.08, rootMargin: '0px 0px -40px 0px' });
    for (var m = 0; m < sections.length; m++) {
      sections[m].classList.add('reveal-ready');
      observer.observe(sections[m]);
    }
  }

  // Smooth scroll for anchor links
  document.addEventListener('click', function (e) {
    var link = e.target.closest('a[href^="#"]');
    if (!link) return;
    var id = link.getAttribute('href');
    if (id.length < 2) return;
    var target = document.querySelector(id);
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      if (header) header.classList.remove('nav-open');
    }
  });

  // Close mobile menu on resize to desktop
  window.addEventListener('resize', function () {
    if (window.innerWidth > 1024 && header) {
      header.classList.remove('nav-open');
      var openSubs = document.querySelectorAll('.sub-open');
      for (var n = 0; n < openSubs.length; n++) openSubs[n].classList.remove('sub-open');
    }
  });
})();
