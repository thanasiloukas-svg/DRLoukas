(function () {
  var canvas = document.getElementById('bg-canvas');
  if (!canvas) return;
  var ctx = canvas.getContext('2d');
  var W, H, particles, mouse, geometrics, sparkles;
  var PARTICLE_COUNT = 110;
  var CONNECTION_DIST = 140;
  var MOUSE_RADIUS = 200;
  var TEAL = { r: 24, g: 198, b: 179 };

  function resize() {
    W = canvas.width = window.innerWidth;
    H = canvas.height = Math.max(window.innerHeight * 1.15, 700);
    canvas.style.width = W + 'px';
    canvas.style.height = H + 'px';
  }

  function createParticles() {
    particles = [];
    for (var i = 0; i < PARTICLE_COUNT; i++) {
      particles.push({
        x: Math.random() * W,
        y: Math.random() * H,
        vx: (Math.random() - 0.5) * 0.7,
        vy: (Math.random() - 0.5) * 0.7,
        r: Math.random() * 2.5 + 1,
        alpha: Math.random() * 0.5 + 0.3,
        pulse: Math.random() * Math.PI * 2
      });
    }
  }

  function createGeometrics() {
    geometrics = [];
    var count = Math.floor(W / 300);
    for (var i = 0; i < count; i++) {
      geometrics.push({
        x: Math.random() * W,
        y: Math.random() * H * 0.8,
        size: Math.random() * 30 + 20,
        rotation: Math.random() * Math.PI,
        rotSpeed: (Math.random() - 0.5) * 0.003,
        type: Math.random() > 0.5 ? 'hex' : 'diamond',
        alpha: Math.random() * 0.08 + 0.03,
        vy: (Math.random() - 0.5) * 0.15
      });
    }
  }

  function createSparkles() {
    sparkles = [];
    for (var i = 0; i < 12; i++) {
      sparkles.push({
        x: Math.random() * W,
        y: Math.random() * H,
        life: Math.random() * 200,
        maxLife: 200 + Math.random() * 150,
        size: Math.random() * 3 + 1.5
      });
    }
  }

  mouse = { x: W / 2, y: H / 2, active: false };

  function onMove(e) {
    var rect = canvas.getBoundingClientRect();
    var clientX = e.touches ? e.touches[0].clientX : e.clientX;
    var clientY = e.touches ? e.touches[0].clientY : e.clientY;
    mouse.x = clientX - rect.left;
    mouse.y = clientY - rect.top;
    mouse.active = true;
  }

  canvas.addEventListener('mousemove', onMove);
  canvas.addEventListener('touchmove', onMove, { passive: true });
  canvas.addEventListener('mouseleave', function () { mouse.active = false; });

  function drawHex(cx, cy, size, rotation) {
    ctx.beginPath();
    for (var i = 0; i < 6; i++) {
      var angle = rotation + (Math.PI / 3) * i;
      var px = cx + size * Math.cos(angle);
      var py = cy + size * Math.sin(angle);
      if (i === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.closePath();
  }

  function drawDiamond(cx, cy, size, rotation) {
    ctx.beginPath();
    for (var i = 0; i < 4; i++) {
      var angle = rotation + (Math.PI / 2) * i;
      var s = i % 2 === 0 ? size * 1.2 : size * 0.7;
      var px = cx + s * Math.cos(angle);
      var py = cy + s * Math.sin(angle);
      if (i === 0) ctx.moveTo(px, py);
      else ctx.lineTo(px, py);
    }
    ctx.closePath();
  }

  function drawSmileArc(time) {
    var cx = W * 0.5;
    var cy = H * 0.45;
    var radius = Math.min(W, H) * 0.18;
    var wobble = Math.sin(time * 0.0008) * 0.05;
    ctx.beginPath();
    ctx.arc(cx, cy, radius, 0.15 + wobble, Math.PI - 0.15 - wobble);
    ctx.strokeStyle = 'rgba(24, 198, 179, 0.06)';
    ctx.lineWidth = 2;
    ctx.stroke();
  }

  function drawWaveMesh(time) {
    ctx.beginPath();
    var step = 60;
    var amp = 15;
    for (var x = 0; x < W + step; x += step) {
      var y = H * 0.85 + Math.sin(x * 0.008 + time * 0.001) * amp;
      if (x === 0) ctx.moveTo(x, y);
      else ctx.lineTo(x, y);
    }
    ctx.strokeStyle = 'rgba(24, 198, 179, 0.07)';
    ctx.lineWidth = 1;
    ctx.stroke();

    ctx.beginPath();
    for (var x2 = 0; x2 < W + step; x2 += step) {
      var y2 = H * 0.88 + Math.sin(x2 * 0.006 + time * 0.0008 + 1) * amp * 0.7;
      if (x2 === 0) ctx.moveTo(x2, y2);
      else ctx.lineTo(x2, y2);
    }
    ctx.strokeStyle = 'rgba(24, 198, 179, 0.04)';
    ctx.lineWidth = 1;
    ctx.stroke();
  }

  var startTime = Date.now();

  function draw() {
    var time = Date.now() - startTime;
    ctx.clearRect(0, 0, W, H);

    drawSmileArc(time);
    drawWaveMesh(time);

    for (var g = 0; g < geometrics.length; g++) {
      var geo = geometrics[g];
      geo.rotation += geo.rotSpeed;
      geo.y += geo.vy;
      if (geo.y < -60) geo.y = H + 60;
      if (geo.y > H + 60) geo.y = -60;
      ctx.save();
      if (geo.type === 'hex') drawHex(geo.x, geo.y, geo.size, geo.rotation);
      else drawDiamond(geo.x, geo.y, geo.size, geo.rotation);
      ctx.strokeStyle = 'rgba(24, 198, 179, ' + geo.alpha + ')';
      ctx.lineWidth = 1;
      ctx.stroke();
      ctx.restore();
    }

    for (var i = 0; i < particles.length; i++) {
      var p = particles[i];
      p.pulse += 0.02;
      var pulseAlpha = p.alpha + Math.sin(p.pulse) * 0.15;

      if (mouse.active) {
        var mdx = p.x - mouse.x;
        var mdy = p.y - mouse.y;
        var md = Math.sqrt(mdx * mdx + mdy * mdy);
        if (md < MOUSE_RADIUS && md > 0) {
          var force = (1 - md / MOUSE_RADIUS) * 0.8;
          p.vx += (mdx / md) * force;
          p.vy += (mdy / md) * force;
        }
      }

      p.vx *= 0.99;
      p.vy *= 0.99;
      p.x += p.vx;
      p.y += p.vy;
      if (p.x < 0) { p.x = 0; p.vx *= -1; }
      if (p.x > W) { p.x = W; p.vx *= -1; }
      if (p.y < 0) { p.y = 0; p.vy *= -1; }
      if (p.y > H) { p.y = H; p.vy *= -1; }

      ctx.beginPath();
      ctx.arc(p.x, p.y, p.r, 0, Math.PI * 2);
      ctx.fillStyle = 'rgba(' + TEAL.r + ',' + TEAL.g + ',' + TEAL.b + ',' + pulseAlpha + ')';
      ctx.fill();

      for (var j = i + 1; j < particles.length; j++) {
        var q = particles[j];
        var dx = p.x - q.x;
        var dy = p.y - q.y;
        var d = dx * dx + dy * dy;
        if (d < CONNECTION_DIST * CONNECTION_DIST) {
          d = Math.sqrt(d);
          ctx.beginPath();
          ctx.moveTo(p.x, p.y);
          ctx.lineTo(q.x, q.y);
          ctx.strokeStyle = 'rgba(24, 198, 179, ' + (1 - d / CONNECTION_DIST) * 0.2 + ')';
          ctx.lineWidth = 0.8;
          ctx.stroke();
        }
      }
    }

    for (var s = 0; s < sparkles.length; s++) {
      var sp = sparkles[s];
      sp.life++;
      if (sp.life > sp.maxLife) {
        sp.x = Math.random() * W;
        sp.y = Math.random() * H;
        sp.life = 0;
        sp.maxLife = 200 + Math.random() * 150;
        sp.size = Math.random() * 3 + 1.5;
      }
      var progress = sp.life / sp.maxLife;
      var sparkAlpha = progress < 0.2 ? progress / 0.2 : progress > 0.8 ? (1 - progress) / 0.2 : 1;
      sparkAlpha *= 0.6;
      if (sparkAlpha > 0.01) {
        ctx.save();
        ctx.translate(sp.x, sp.y);
        ctx.rotate(time * 0.001);
        ctx.beginPath();
        ctx.moveTo(0, -sp.size);
        ctx.lineTo(sp.size * 0.3, 0);
        ctx.lineTo(0, sp.size);
        ctx.lineTo(-sp.size * 0.3, 0);
        ctx.closePath();
        ctx.fillStyle = 'rgba(24, 198, 179, ' + sparkAlpha + ')';
        ctx.fill();
        ctx.restore();
      }
    }

    requestAnimationFrame(draw);
  }

  resize();
  createParticles();
  createGeometrics();
  createSparkles();
  window.addEventListener('resize', function () {
    resize();
    createGeometrics();
  });
  draw();
})();
