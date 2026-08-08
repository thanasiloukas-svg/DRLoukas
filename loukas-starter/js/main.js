(function () {
  // Mobile menu toggle
  var toggle = document.getElementById('mobile-toggle');
  var header = document.getElementById('site-header');
  if (toggle && header) {
    toggle.addEventListener('click', function () {
      header.classList.toggle('nav-open');
    });
  }

  // FAQ accordion
  var faqButtons = document.querySelectorAll('.hp-faq-q');
  for (var i = 0; i < faqButtons.length; i++) {
    faqButtons[i].addEventListener('click', function () {
      var answer = this.nextElementSibling;
      var icon = this.querySelector('.hp-faq-icon');
      var isOpen = answer.style.maxHeight && answer.style.maxHeight !== '0px';
      if (isOpen) {
        answer.style.maxHeight = '0px';
        answer.style.paddingBottom = '0';
        if (icon) icon.style.transform = 'rotate(0deg)';
      } else {
        answer.style.maxHeight = answer.scrollHeight + 20 + 'px';
        answer.style.paddingBottom = '20px';
        if (icon) icon.style.transform = 'rotate(45deg)';
      }
    });
  }

  // Scroll reveal
  var sections = document.querySelectorAll('.hp-section');
  if (sections.length && 'IntersectionObserver' in window) {
    var observer = new IntersectionObserver(function (entries) {
      for (var j = 0; j < entries.length; j++) {
        if (entries[j].isIntersecting) {
          entries[j].target.classList.add('revealed');
          observer.unobserve(entries[j].target);
        }
      }
    }, { threshold: 0.1 });
    for (var k = 0; k < sections.length; k++) {
      sections[k].classList.add('reveal-ready');
      observer.observe(sections[k]);
    }
  }

  // Smooth scroll for anchor links
  document.addEventListener('click', function (e) {
    var link = e.target.closest('a[href^="#"]');
    if (!link) return;
    var target = document.querySelector(link.getAttribute('href'));
    if (target) {
      e.preventDefault();
      target.scrollIntoView({ behavior: 'smooth', block: 'start' });
      if (header) header.classList.remove('nav-open');
    }
  });
})();
