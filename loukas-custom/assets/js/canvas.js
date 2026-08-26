document.addEventListener('DOMContentLoaded', function () {
  var c = document.getElementById('bg-canvas');
  if (!c) return;
  var ctx = c.getContext('2d');
  var W, H, particles, ripples, mouse, frame;
  var TOTAL = 120;
  var CONN_DIST = 150;
  var MOUSE_RADIUS = 220;
  var SMILE_INTERVAL = 400;
  var SMILE_HOLD = 180;
  var LERP_SPEED = 0.035;
  var isForming = false;
  var formFrame = 0;
  var smileTargets = null;

  function resize() {
    W = c.width = window.innerWidth;
    H = c.height = Math.floor(window.innerHeight * 1.1);
    c.style.width = W + 'px';
    c.style.height = H + 'px';
  }

  function createParticles() {
    particles = [];
    for (var i = 0; i < TOTAL; i++) {
      particles.push({
        x: Math.random() * W,
        y: Math.random() * H,
        vx: (Math.random() - 0.5) * 1.4,
        vy: (Math.random() - 0.5) * 1.4,
        r: Math.random() * 3.2 + 1.2,
        alpha: 0.3 + Math.random() * 0.5,
        pulse: Math.random() * Math.PI * 2
      });
    }
  }

  mouse = { x: -9999, y: -9999, active: false };
  ripples = [];
  frame = 0;

  function onMove(e) {
    var rect = c.getBoundingClientRect();
    var cx = e.touches ? e.touches[0].clientX : e.clientX;
    var cy = e.touches ? e.touches[0].clientY : e.clientY;
    mouse.x = cx - rect.left;
    mouse.y = cy - rect.top;
    mouse.active = true;
  }

  c.addEventListener('mousemove', onMove);
  c.addEventListener('touchmove', onMove, { passive: true });
  c.addEventListener('mouseleave', function () { mouse.active = false; });

  c.addEventListener('click', function (e) {
    var rect = c.getBoundingClientRect();
    var cx = e.clientX - rect.left;
    var cy = e.clientY - rect.top;
    ripples.push({ x: cx, y: cy, r: 0, maxR: 120, alpha: 0.5 });
    for (var i = 0; i < 12; i++) {
      var angle = (Math.PI * 2 / 12) * i;
      var speed = 2 + Math.random() * 3;
      particles.push({
        x: cx, y: cy,
        vx: Math.cos(angle) * speed,
        vy: Math.sin(angle) * speed,
        r: Math.random() * 2 + 1,
        alpha: 0.7,
        pulse: 0,
        burst: true,
        born: frame
      });
    }
    if (isForming) {
      isForming = false;
      smileTargets = null;
      releaseParticles();
    }
  });

  c.addEventListener('touchstart', function (e) {
    var t = e.touches[0];
    var rect = c.getBoundingClientRect();
    var cx = t.clientX - rect.left;
    var cy = t.clientY - rect.top;
    ripples.push({ x: cx, y: cy, r: 0, maxR: 120, alpha: 0.5 });
  }, { passive: true });

  function buildSmileTargets() {
    var targets = [];
    var cx = W / 2;
    var cy = H * 0.44;
    var radius = Math.min(W, H) * 0.22;
    var smileCount = Math.floor(TOTAL * 0.68);
    var eyeCount = Math.floor(TOTAL * 0.16);
    for (var i = 0; i < smileCount; i++) {
      var t = i / (smileCount - 1);
      var angle = 0.15 * Math.PI + t * 0.7 * Math.PI;
      targets.push({ x: cx + Math.cos(angle) * radius, y: cy + Math.sin(angle) * radius });
    }
    var leftCx = cx - radius * 0.45;
    var leftCy = cy - radius * 0.5;
    var rightCx = cx + radius * 0.45;
    var rightCy = cy - radius * 0.5;
    var erx = radius * 0.12;
    var ery = radius * 0.18;
    for (var j = 0; j < eyeCount; j++) {
      var ea = (Math.PI * 2 / eyeCount) * j;
      targets.push({ x: leftCx + Math.cos(ea) * erx, y: leftCy + Math.sin(ea) * ery });
    }
    for (var k = 0; k < eyeCount; k++) {
      var ea2 = (Math.PI * 2 / eyeCount) * k;
      targets.push({ x: rightCx + Math.cos(ea2) * erx, y: rightCy + Math.sin(ea2) * ery });
    }
    return targets;
  }

  function releaseParticles() {
    for (var i = 0; i < TOTAL && i < particles.length; i++) {
      particles[i].vx = (Math.random() - 0.5) * 1.4;
      particles[i].vy = (Math.random() - 0.5) * 1.4;
    }
  }

  function draw() {
    frame++;
    ctx.clearRect(0, 0, W, H);

    // Glow effect following mouse
    if (mouse.active) {
      var grd = ctx.createRadialGradient(mouse.x, mouse.y, 0, mouse.x, mouse.y, 250);
      grd.addColorStop(0, 'rgba(24,198,179,0.06)');
      grd.addColorStop(1, 'rgba(24,198,179,0)');
      ctx.fillStyle = grd;
      ctx.fillRect(0, 0, W, H);
    }

    // Smile formation logic
    if (!isForming && frame % SMILE_INTERVAL === 0 && frame > 60) {
      isForming = true;
      formFrame = 0;
      smileTargets = buildSmileTargets();
    }
    if (isForming) {
      formFrame++;
      if (formFrame > SMILE_HOLD) {
        isForming = false;
        smileTargets = null;
        releaseParticles();
      }
    }

    // Remove expired burst particles
    var cleaned = [];
    for (var b = 0; b < particles.length; b++) {
      if (particles[b].burst && frame - particles[b].born > 150) continue;
      cleaned.push(particles[b]);
    }
    particles = cleaned;

    // Update and draw particles
    for (var i = 0; i < particles.length; i++) {
      var p = particles[i];
      p.pulse += 0.02;

      if (isForming && smileTargets && i < smileTargets.length && i < TOTAL) {
        var tx = smileTargets[i].x;
        var ty = smileTargets[i].y;
        p.x += (tx - p.x) * LERP_SPEED;
        p.y += (ty - p.y) * LERP_SPEED;
        p.vx *= 0.9;
        p.vy *= 0.9;
      } else {
        // Mouse attraction
        if (mouse.active) {
          var mdx = mouse.x - p.x;
          var mdy = mouse.y - p.y;
          var md = Math.sqrt(mdx * mdx + mdy * mdy);
          if (md < MOUSE_RADIUS && md > 1) {
            var force = (1 - md / MOUSE_RADIUS) * 0.15;
            p.vx += (mdx / md) * force;
            p.vy += (mdy / md) * force;
          }
        }

        p.vx *= 0.995;
        p.vy *= 0.995;
        p.x += p.vx;
        p.y += p.vy;

        // Wrap around edges
        if (p.x < -10) p.x = W + 10;
        else if (p.x > W + 10) p.x = -10;
        if (p.y < -10) p.y = H + 10;
        else if (p.y > H + 10) p.y = -10;
      }

      var pulseAlpha = p.alpha + Math.sin(p.pulse) * 0.15;
      if (p.burst) {
        var age = frame - p.born;
        pulseAlpha *= Math.max(0, 1 - age / 150);
      }

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(24,198,179,' + Math.max(0, pulseAlpha) + ')';
      ctx.fill();

      // Connections
      for (var j = i + 1; j < particles.length; j++) {
        var q = particles[j];
        var dx = p.x - q.x;
        var dy = p.y - q.y;
        var dsq = dx * dx + dy * dy;
        if (dsq < CONN_DIST * CONN_DIST) {
          var d = Math.sqrt(dsq);
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(q.x, q.y);
          ctx.strokeStyle = 'rgba(24,198,179,' + (1 - d / CONN_DIST) * 0.2 + ')';
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }
      }
    }

    // Draw ripples
    for (var r = ripples.length - 1; r >= 0; r--) {
      var rp = ripples[r];
      rp.r += 3;
      rp.alpha -= 0.012;
      if (rp.alpha <= 0) {
        ripples.splice(r, 1);
        continue;
      }
      ctx.beginPath();
      ctx.arc(rp.x, rp.y, rp.r, 0, Math.PI * 2);
      ctx.strokeStyle = 'rgba(24,198,179,' + rp.alpha + ')';
      ctx.lineWidth = 2;
      ctx.stroke();
    }

    requestAnimationFrame(draw);
  }

  resize();
  createParticles();
  window.addEventListener('resize', function () {
    resize();
    smileTargets = null;
  });
  draw();
});
