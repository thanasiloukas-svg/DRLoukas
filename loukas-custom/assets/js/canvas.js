document.addEventListener('DOMContentLoaded', function () {
  var c = document.getElementById('bg-canvas');
  if (!c) return;
  var ctx = c.getContext('2d');
  var W, H, particles, ripples, mouse, frame;
  var TOTAL = 120;
  var CONN_DIST = 150;
  var MOUSE_RADIUS = 220;
  var FORM_INTERVAL = 500;
  var FORM_HOLD = 200;
  var LERP_SPEED = 0.035;
  var isForming = false;
  var formFrame = 0;
  var formTargets = null;
  var formIndex = -1;
  var pendingSwitch = 0;

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

  function buildSmiley(scale) {
    var targets = [];
    var fcx = W / 2;
    var fcy = H * 0.44;
    var radius = Math.min(W, H) * 0.22 * scale;
    var smileCount = Math.floor(TOTAL * 0.68);
    var eyeCount = Math.floor(TOTAL * 0.16);

    for (var i = 0; i < smileCount; i++) {
      var t = i / (smileCount - 1);
      var angle = 0.15 * Math.PI + t * 0.7 * Math.PI;
      targets.push({ x: fcx + Math.cos(angle) * radius, y: fcy + Math.sin(angle) * radius });
    }

    var lx = fcx - radius * 0.45, ly = fcy - radius * 0.5;
    var rx = fcx + radius * 0.45, ry = fcy - radius * 0.5;
    var erx = radius * 0.12, ery = radius * 0.18;

    for (var j = 0; j < eyeCount; j++) {
      var ea = (Math.PI * 2 / eyeCount) * j;
      targets.push({ x: lx + Math.cos(ea) * erx, y: ly + Math.sin(ea) * ery });
    }
    for (var k = 0; k < eyeCount; k++) {
      var ea2 = (Math.PI * 2 / eyeCount) * k;
      targets.push({ x: rx + Math.cos(ea2) * erx, y: ry + Math.sin(ea2) * ery });
    }
    return targets;
  }

  function buildTeeth() {
    var targets = [];
    var fcx = W / 2;
    var fcy = H * 0.44;
    var radius = Math.min(W, H) * 0.22;
    var numTeeth = 8;
    var pPerTooth = 6;
    var toothW = radius * 0.07;
    var toothH = radius * 0.14;

    for (var t = 0; t < numTeeth; t++) {
      var frac = (t + 0.5) / numTeeth;
      var angle = Math.PI + frac * Math.PI;
      var tcx = fcx + Math.cos(angle) * radius * 0.7;
      var tcy = fcy - radius * 0.08 + Math.sin(angle) * radius * 0.18;
      for (var p = 0; p < pPerTooth; p++) {
        var col = (p % 2 - 0.5) * toothW;
        var row = (Math.floor(p / 2) - 1) * (toothH / 2.5);
        targets.push({ x: tcx + col, y: tcy + row });
      }
    }

    for (var t2 = 0; t2 < numTeeth; t2++) {
      var frac2 = (t2 + 0.5) / numTeeth;
      var angle2 = frac2 * Math.PI;
      var tcx2 = fcx + Math.cos(angle2) * radius * 0.65;
      var tcy2 = fcy + radius * 0.2 + Math.sin(angle2) * radius * 0.14;
      for (var p2 = 0; p2 < pPerTooth; p2++) {
        var col2 = (p2 % 2 - 0.5) * toothW * 0.9;
        var row2 = (Math.floor(p2 / 2) - 1) * (toothH / 2.5);
        targets.push({ x: tcx2 + col2, y: tcy2 - row2 });
      }
    }

    var used = numTeeth * pPerTooth * 2;
    var remaining = TOTAL - used;
    for (var l = 0; l < remaining; l++) {
      var lt = l / Math.max(remaining - 1, 1);
      var la = lt * Math.PI;
      targets.push({
        x: fcx + Math.cos(la + Math.PI * 0.5) * radius * 0.9,
        y: fcy + Math.sin(la) * radius * 0.5
      });
    }
    return targets;
  }

  function buildGrin() {
    var targets = [];
    var fcx = W / 2;
    var fcy = H * 0.44;
    var radius = Math.min(W, H) * 0.27;
    var smileCount = Math.floor(TOTAL * 0.48);
    var teethCount = Math.floor(TOTAL * 0.22);
    var eyeCount = Math.floor(TOTAL * 0.15);
    var halfEye = Math.floor(eyeCount / 2);

    for (var i = 0; i < smileCount; i++) {
      var t = i / (smileCount - 1);
      var angle = 0.08 * Math.PI + t * 0.84 * Math.PI;
      targets.push({
        x: fcx + Math.cos(angle) * radius,
        y: fcy + Math.sin(angle) * radius * 0.65
      });
    }

    for (var j = 0; j < teethCount; j++) {
      var tt = (j + 0.5) / teethCount;
      var tx = fcx + (tt - 0.5) * radius * 1.7;
      var archCurve = Math.pow((tt - 0.5) * 2, 2) * radius * 0.15;
      targets.push({ x: tx, y: fcy + radius * 0.12 - archCurve });
    }

    var lx = fcx - radius * 0.38, ly = fcy - radius * 0.38;
    var rx = fcx + radius * 0.38, ry = fcy - radius * 0.38;
    var eyeW = radius * 0.14;

    for (var k = 0; k < halfEye; k++) {
      var et = k / Math.max(halfEye - 1, 1);
      targets.push({
        x: lx + (et - 0.5) * eyeW * 2,
        y: ly - Math.abs(et - 0.5) * radius * 0.08
      });
    }
    for (var m = 0; m < halfEye; m++) {
      var et2 = m / Math.max(halfEye - 1, 1);
      targets.push({
        x: rx + (et2 - 0.5) * eyeW * 2,
        y: ry - Math.abs(et2 - 0.5) * radius * 0.08
      });
    }

    while (targets.length < TOTAL) {
      var fi = targets.length / TOTAL;
      targets.push({
        x: fcx + (fi - 0.5) * radius * 0.5,
        y: fcy + radius * 0.3
      });
    }
    return targets;
  }

  var formations = [
    function () { return buildSmiley(1); },
    function () { return buildTeeth(); },
    function () { return buildSmiley(0.55); },
    function () { return buildGrin(); }
  ];

  function nextFormation() {
    formIndex = (formIndex + 1) % formations.length;
    isForming = true;
    formFrame = 0;
    formTargets = formations[formIndex]();
  }

  function releaseParticles() {
    for (var i = 0; i < TOTAL && i < particles.length; i++) {
      particles[i].vx = (Math.random() - 0.5) * 1.4;
      particles[i].vy = (Math.random() - 0.5) * 1.4;
    }
  }

  function handleInteraction(px, py) {
    ripples.push({ x: px, y: py, r: 0, maxR: 120, alpha: 0.5 });
    for (var i = 0; i < 12; i++) {
      var angle = (Math.PI * 2 / 12) * i;
      var speed = 2 + Math.random() * 3;
      particles.push({
        x: px, y: py,
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
      formTargets = null;
      releaseParticles();
    }
    pendingSwitch = 18;
  }

  c.addEventListener('click', function (e) {
    var rect = c.getBoundingClientRect();
    handleInteraction(e.clientX - rect.left, e.clientY - rect.top);
  });

  c.addEventListener('touchstart', function (e) {
    var t = e.touches[0];
    var rect = c.getBoundingClientRect();
    handleInteraction(t.clientX - rect.left, t.clientY - rect.top);
  }, { passive: true });

  function draw() {
    frame++;
    ctx.clearRect(0, 0, W, H);

    if (mouse.active) {
      var grd = ctx.createRadialGradient(mouse.x, mouse.y, 0, mouse.x, mouse.y, 250);
      grd.addColorStop(0, 'rgba(24,198,179,0.06)');
      grd.addColorStop(1, 'rgba(24,198,179,0)');
      ctx.fillStyle = grd;
      ctx.fillRect(0, 0, W, H);
    }

    if (pendingSwitch > 0) {
      pendingSwitch--;
      if (pendingSwitch === 0) nextFormation();
    }

    if (!isForming && pendingSwitch === 0 && frame % FORM_INTERVAL === 0 && frame > 60) {
      nextFormation();
    }

    if (isForming) {
      formFrame++;
      if (formFrame > FORM_HOLD) {
        isForming = false;
        formTargets = null;
        releaseParticles();
      }
    }

    var cleaned = [];
    for (var b = 0; b < particles.length; b++) {
      if (particles[b].burst && frame - particles[b].born > 150) continue;
      cleaned.push(particles[b]);
    }
    particles = cleaned;

    for (var i = 0; i < particles.length; i++) {
      var p = particles[i];
      p.pulse += 0.02;

      if (isForming && formTargets && i < formTargets.length && i < TOTAL) {
        p.x += (formTargets[i].x - p.x) * LERP_SPEED;
        p.y += (formTargets[i].y - p.y) * LERP_SPEED;
        p.vx *= 0.9;
        p.vy *= 0.9;
      } else {
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
        if (p.x < -10) p.x = W + 10;
        else if (p.x > W + 10) p.x = -10;
        if (p.y < -10) p.y = H + 10;
        else if (p.y > H + 10) p.y = -10;
      }

      var pulseAlpha = p.alpha + Math.sin(p.pulse) * 0.15;
      if (p.burst) {
        pulseAlpha *= Math.max(0, 1 - (frame - p.born) / 150);
      }

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(24,198,179,' + Math.max(0, pulseAlpha) + ')';
      ctx.fill();

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
    formTargets = null;
  });
  draw();
});
