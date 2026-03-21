<!DOCTYPE html>
<html lang="en">
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">
<title>Smart Gateway — README</title>
<link href="https://fonts.googleapis.com/css2?family=Share+Tech+Mono&family=Barlow+Condensed:wght@700;900&family=Barlow:wght@300;400;600;700&display=swap" rel="stylesheet">
<style>
*{margin:0;padding:0;box-sizing:border-box}
body{background:#0a0e1a;color:#c8dff0;font-family:'Barlow',sans-serif;line-height:1.6}
.page{max-width:900px;margin:0 auto;padding:40px 32px 80px}

/* ── INDIAN TRICOLOUR BANNER ── */
/* Saffron:#FF9933  White:#FFFFFF  Green:#138808  Chakra Navy:#000080 */
.banner{position:relative;overflow:hidden;padding:48px 40px 40px;margin-bottom:48px;border:1px solid rgba(255,153,51,0.2)}
.banner-stripe-bg{position:absolute;inset:0;display:flex;flex-direction:column}
.s{flex:1}
.s1,.s4,.s7{background:#FF9933}
.s2,.s5,.s8{background:#f5f5f0}
.s3,.s6,.s9{background:#138808}
.banner-overlay{position:absolute;inset:0;background:rgba(4,8,18,0.86)}
.banner-content{position:relative;z-index:2;text-align:center}
.banner-eyebrow{font-family:'Share Tech Mono',monospace;font-size:11px;letter-spacing:4px;color:#bba;text-transform:uppercase;margin-bottom:16px}
.banner-ascii{font-family:'Share Tech Mono',monospace;font-size:clamp(5px,1.2vw,11px);line-height:1.15;white-space:pre;margin-bottom:20px}
.ascii-s{color:#FF9933} .ascii-m{color:#ffffff} .ascii-g{color:#138808}
.banner-title{font-family:'Barlow Condensed',sans-serif;font-size:clamp(36px,7vw,72px);font-weight:900;text-transform:uppercase;letter-spacing:-1px;line-height:1;margin-bottom:12px}
.t-r{color:#FF9933} .t-w{color:#ffffff} .t-b{color:#138808}
.banner-tagline{font-size:15px;font-weight:300;color:#c8dfc8;font-style:italic;margin-bottom:24px}
.chakra{font-size:28px;margin-bottom:12px;color:#000080;filter:drop-shadow(0 0 6px #000080aa)}
.badges{display:flex;flex-wrap:wrap;gap:8px;justify-content:center;margin-bottom:20px}
.badge{font-family:'Share Tech Mono',monospace;font-size:10px;padding:5px 12px;border-radius:3px;font-weight:400;text-transform:uppercase;letter-spacing:1px}
.b-py{background:#2a1a00;color:#FF9933;border:1px solid #663d00}
.b-nm{background:#0a2010;color:#33cc66;border:1px solid #138808}
.b-ts{background:#00001a;color:#6699ff;border:1px solid #000080}
.b-ml{background:#2a1a00;color:#ffbb44;border:1px solid #996600}
.b-mt{background:#0a2010;color:#66dd88;border:1px solid #138808}
.tribar{display:flex;gap:16px;justify-content:center;align-items:center;margin-top:4px}
.tribar-dot{width:10px;height:10px;border-radius:50%}
.td1{background:#FF9933;box-shadow:0 0 8px #FF993388}
.td2{background:#ffffff;box-shadow:0 0 8px #ffffff44}
.td3{background:#138808;box-shadow:0 0 8px #13880888}
.tribar-line{width:40px;height:2px}
.tl1{background:#FF9933} .tl2{background:#ffffff} .tl3{background:#138808}

/* ── SECTIONS ── */
.section{margin-bottom:56px}
.section-label{font-family:'Share Tech Mono',monospace;font-size:10px;color:#FF9933;letter-spacing:3px;text-transform:uppercase;margin-bottom:8px}
.section-title{font-family:'Barlow Condensed',sans-serif;font-size:32px;font-weight:900;text-transform:uppercase;color:#fff;margin-bottom:16px;letter-spacing:-0.5px}
.prose{font-size:15px;color:#aabba8;line-height:1.7;max-width:700px}
.prose strong{color:#e8f5e8;font-weight:600}
.divider{border:none;border-top:1px solid rgba(255,153,51,0.12);margin:48px 0}

/* ── FLOWCHART CARDS ── */
.fc-card{background:#050e08;border:1px solid rgba(19,136,8,0.2);border-top:2px solid;margin-bottom:32px;overflow:hidden}
.fc-card:nth-child(1){border-top-color:#FF9933}
.fc-card:nth-child(2){border-top-color:#138808}
.fc-card:nth-child(3){border-top-color:#FF9933}
.fc-card:nth-child(4){border-top-color:#138808}
.fc-card:nth-child(5){border-top-color:#ffffff}
.fc-header{padding:14px 20px;border-bottom:1px solid rgba(19,136,8,0.15);display:flex;align-items:center;gap:12px}
.fc-num{font-family:'Share Tech Mono',monospace;font-size:10px;color:#FF9933;border:1px solid #FF9933;padding:3px 8px}
.fc-title{font-size:14px;font-weight:600;color:#fff}
.fc-sub{font-size:12px;color:#567}
.fc-body{padding:20px}
.fc-body svg{width:100%;display:block}

/* ── TOOLS TABLE ── */
.tools-table{width:100%;border-collapse:collapse;margin-top:16px}
.tools-table th{font-family:'Share Tech Mono',monospace;font-size:10px;letter-spacing:2px;text-transform:uppercase;color:#FF9933;padding:10px 14px;border-bottom:2px solid rgba(255,153,51,0.3);text-align:left}
.tools-table td{padding:12px 14px;border-bottom:1px solid rgba(19,136,8,0.1);font-size:14px;vertical-align:top}
.tools-table tr:hover td{background:rgba(19,136,8,0.05)}
.tool-name{font-family:'Share Tech Mono',monospace;font-size:12px;color:#fff;font-weight:400}
.tool-cat{font-size:12px;color:#567}
.tool-desc{font-size:13px;color:#7a9978}

/* ── COMPARISON TABLE ── */
.cmp-table{width:100%;border-collapse:collapse;margin-top:16px}
.cmp-table th{font-family:'Share Tech Mono',monospace;font-size:10px;letter-spacing:2px;color:#FF9933;padding:10px 14px;border-bottom:2px solid rgba(255,153,51,0.3);text-align:center}
.cmp-table th:first-child{text-align:left}
.cmp-table td{padding:10px 14px;border-bottom:1px solid rgba(19,136,8,0.1);font-size:13px;text-align:center;color:#567}
.cmp-table td:first-child{text-align:left;color:#aabba8}
.cmp-table td.yes{color:#4dbb88;font-size:15px}
.cmp-table td.no{color:#cc4422;font-size:15px}
.cmp-table td.sg{color:#fff;font-weight:700;font-size:15px}
.cmp-table td.sgno{color:#4dbb88;font-size:15px}

/* ── DEEP DIVE GRID ── */
.deep-grid{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:16px}
@media(max-width:600px){.deep-grid{grid-template-columns:1fr}}
.deep-card{background:#050e08;border:1px solid rgba(19,136,8,0.2);border-left:3px solid #FF9933;padding:18px 20px}
.deep-card:nth-child(even){border-left-color:#138808}
.deep-title{font-size:14px;font-weight:600;color:#fff;margin-bottom:8px}
.deep-card p{font-size:13px;color:#7a9978;line-height:1.6}
.deep-card em{color:#FF9933;font-style:normal}

/* ── CHALLENGES ── */
.challenge-list{display:flex;flex-direction:column;gap:12px;margin-top:16px}
.challenge-item{display:flex;gap:16px;align-items:flex-start;background:#050e08;border:1px solid rgba(19,136,8,0.15);padding:18px 20px}
.ch-num{font-family:'Share Tech Mono',monospace;font-size:11px;color:#FF9933;border:1px solid #FF9933;padding:3px 8px;flex-shrink:0;margin-top:2px}
.ch-title{font-size:14px;font-weight:600;color:#fff;margin-bottom:6px}
.ch-body p{font-size:13px;color:#7a9978;line-height:1.6}

/* ── BOTTOM ROW ── */
.bottom-row{display:grid;grid-template-columns:1fr 1fr;gap:14px;margin-top:16px}
@media(max-width:600px){.bottom-row{grid-template-columns:1fr}}
.bottom-card{background:#050e08;border:1px solid rgba(19,136,8,0.15);padding:20px}
.bottom-icon{font-size:20px;margin-bottom:8px}
.bottom-label{font-size:13px;font-weight:600;color:#fff;margin-bottom:6px}
.bottom-card p{font-size:13px;color:#7a9978;line-height:1.6}

/* ── FOOTER ── */
.footer{text-align:center;padding-top:40px;border-top:1px solid rgba(255,153,51,0.15)}
.footer p{font-family:'Share Tech Mono',monospace;font-size:12px;color:#3a5a3a;line-height:2}
.footer .highlight{color:#FF9933}
</style>
</head>
<body>
<div class="page">

<!-- ═══════════════════════════════ BANNER ═══════════════════════════════ -->
<div class="banner">
  <div class="banner-stripe-bg">
    <div class="s s1"></div><div class="s s2"></div><div class="s s3"></div>
    <div class="s s1"></div><div class="s s2"></div><div class="s s3"></div>
    <div class="s s1"></div><div class="s s2"></div><div class="s s3"></div>
  </div>
  <div class="banner-overlay"></div>
  <div class="banner-content">
    <div class="banner-eyebrow">// AI-Powered Network Defense System</div>
    <pre class="banner-ascii"><span class="ascii-s">███████╗</span><span class="ascii-m">███╗   ███╗ █████╗ ██████╗ ████████╗</span>     <span class="ascii-g">██████╗  █████╗ ████████╗███████╗██╗    ██╗ █████╗ ██╗   ██╗</span>
<span class="ascii-s">██╔════╝</span><span class="ascii-m">████╗ ████║██╔══██╗██╔══██╗╚══██╔══╝</span>    <span class="ascii-g">██╔════╝ ██╔══██╗╚══██╔══╝██╔════╝██║    ██║██╔══██╗╚██╗ ██╔╝</span>
<span class="ascii-s">███████╗</span><span class="ascii-m">██╔████╔██║███████║██████╔╝   ██║   </span>    <span class="ascii-g">██║  ███╗███████║   ██║   █████╗  ██║ █╗ ██║███████║ ╚████╔╝ </span>
<span class="ascii-s">╚════██║</span><span class="ascii-m">██║╚██╔╝██║██╔══██║██╔══██╗   ██║   </span>    <span class="ascii-g">██║   ██║██╔══██║   ██║   ██╔══╝  ██║███╗██║██╔══██║  ╚██╔╝  </span>
<span class="ascii-s">███████║</span><span class="ascii-m">██║ ╚═╝ ██║██║  ██║██║  ██║   ██║   </span>    <span class="ascii-g">╚██████╔╝██║  ██║   ██║   ███████╗╚███╔███╔╝██║  ██║   ██║   </span>
<span class="ascii-s">╚══════╝</span><span class="ascii-m">╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝   </span>    <span class="ascii-g"> ╚═════╝ ╚═╝  ╚═╝   ╚═╝   ╚══════╝ ╚══╝╚══╝ ╚═╝  ╚═╝   ╚═╝   </span></pre>
    <div class="banner-title">
      <span class="t-r">Smart</span>&nbsp;<span class="t-b">Gateway</span>
    </div>
    <div class="banner-tagline">🔐 Your network's silent guardian. Always watching. Never sleeping.</div>
    <div class="badges">
      <span class="badge b-py">Python 3.8+</span>
      <span class="badge b-nm">Nmap</span>
      <span class="badge b-ts">TShark</span>
      <span class="badge b-ml">Isolation Forest</span>
      <span class="badge b-mt">MIT License</span>
    </div>
    <div class="chakra">☸</div>
    <div class="tribar">
      <div class="tribar-line tl1"></div>
      <div class="tribar-dot td1"></div>
      <div class="tribar-line tl1"></div>
      <div style="width:8px"></div>
      <div class="tribar-line tl2"></div>
      <div class="tribar-dot td2"></div>
      <div class="tribar-line tl2"></div>
      <div style="width:8px"></div>
      <div class="tribar-line tl3"></div>
      <div class="tribar-dot td3"></div>
      <div class="tribar-line tl3"></div>
    </div>
  </div>
</div>

<!-- ═══════════════════════════════ STORY ═══════════════════════════════ -->
<div class="section">
  <div class="section-label">// 01 — The Story</div>
  <div class="section-title">Networks see. They don't understand.</div>
  <p class="prose">Most network security tools are glorified loggers. Nmap tells you what's on your network. Wireshark shows you every packet. But neither will stop the hacked IoT device flooding your network at 2am. Neither will notice the machine quietly running in promiscuous mode reading everyone's traffic. Neither will catch the MAC spoofer pretending to be your trusted server.<br><br><strong>Smart Gateway does.</strong> It watches your network the way a security analyst would — learning what normal looks like, spotting when something breaks that pattern, and acting before you even open your laptop.</p>
</div>

<hr class="divider">

<!-- ═══════════════════════════════ FLOWCHARTS ═══════════════════════════ -->
<div class="section">
  <div class="section-label">// 02 — System Flowcharts</div>
  <div class="section-title">How it all works</div>

  <!-- FLOWCHART 1 -->
  <div class="fc-card">
    <div class="fc-header">
      <span class="fc-num">01</span>
      <div><div class="fc-title">Overall system flow</div><div class="fc-sub">End-to-end from scanning to response</div></div>
    </div>
    <div class="fc-body">
<svg viewBox="0 0 680 520" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="a1" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<!-- Nmap -->
<rect x="60" y="40" width="180" height="56" rx="8" fill="#0d1f38" stroke="#185FA5" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#85B7EB" x="150" y="63" text-anchor="middle" dominant-baseline="central">Nmap scanner</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#378ADD" x="150" y="82" text-anchor="middle" dominant-baseline="central">Device discovery</text>
<!-- TShark -->
<rect x="440" y="40" width="180" height="56" rx="8" fill="#0d1f38" stroke="#185FA5" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#85B7EB" x="530" y="63" text-anchor="middle" dominant-baseline="central">TShark capture</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#378ADD" x="530" y="82" text-anchor="middle" dominant-baseline="central">Live traffic analysis</text>
<!-- arrows merge -->
<line x1="150" y1="96" x2="150" y2="150" stroke="#378ADD" stroke-width="1" marker-end="url(#a1)"/>
<line x1="150" y1="150" x2="300" y2="150" stroke="#378ADD" stroke-width="1" marker-end="url(#a1)"/>
<line x1="530" y1="96" x2="530" y2="150" stroke="#378ADD" stroke-width="1" marker-end="url(#a1)"/>
<line x1="530" y1="150" x2="390" y2="150" stroke="#378ADD" stroke-width="1" marker-end="url(#a1)"/>
<!-- Feature Eng -->
<rect x="250" y="130" width="180" height="56" rx="8" fill="#1a0d38" stroke="#534AB7" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#AFA9EC" x="340" y="153" text-anchor="middle" dominant-baseline="central">Feature engineering</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#7F77DD" x="340" y="172" text-anchor="middle" dominant-baseline="central">JSON → ML features</text>
<line x1="340" y1="186" x2="340" y2="226" stroke="#7F77DD" stroke-width="1" marker-end="url(#a1)"/>
<!-- Isolation Forest -->
<rect x="250" y="226" width="180" height="56" rx="8" fill="#1a0d38" stroke="#534AB7" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#AFA9EC" x="340" y="249" text-anchor="middle" dominant-baseline="central">Isolation Forest</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#7F77DD" x="340" y="268" text-anchor="middle" dominant-baseline="central">Anomaly scoring</text>
<line x1="340" y1="282" x2="340" y2="318" stroke="#7F77DD" stroke-width="1" marker-end="url(#a1)"/>
<!-- Decision diamond -->
<polygon points="340,318 415,356 340,394 265,356" fill="#0a0e1a" stroke="#534AB7" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#AFA9EC" x="340" y="352" text-anchor="middle" dominant-baseline="central">Threat?</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#7F77DD" x="340" y="370" text-anchor="middle" dominant-baseline="central">score &gt; threshold</text>
<!-- YES -->
<line x1="340" y1="394" x2="340" y2="434" stroke="#D85A30" stroke-width="1" marker-end="url(#a1)"/>
<text font-family="Barlow,sans-serif" font-size="11" fill="#D85A30" x="350" y="418">yes</text>
<!-- NO -->
<line x1="415" y1="356" x2="575" y2="356" stroke="#5F5E5A" stroke-width="1" marker-end="url(#a1)"/>
<text font-family="Barlow,sans-serif" font-size="11" fill="#888780" x="488" y="348">no</text>
<rect x="520" y="332" width="120" height="48" rx="8" fill="#0f1a10" stroke="#3B6D11" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#97C459" x="580" y="352" text-anchor="middle" dominant-baseline="central">Continue</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#639922" x="580" y="370" text-anchor="middle" dominant-baseline="central">monitoring</text>
<!-- 3 response boxes -->
<rect x="60" y="434" width="150" height="52" rx="8" fill="#250d05" stroke="#993C1D" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#F0997B" x="135" y="456" text-anchor="middle" dominant-baseline="central">Block device</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#D85A30" x="135" y="474" text-anchor="middle" dominant-baseline="central">Auto isolate</text>
<rect x="265" y="434" width="150" height="52" rx="8" fill="#25190a" stroke="#854F0B" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#EF9F27" x="340" y="456" text-anchor="middle" dominant-baseline="central">Email alert</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#BA7517" x="340" y="474" text-anchor="middle" dominant-baseline="central">Notify admin</text>
<rect x="470" y="434" width="150" height="52" rx="8" fill="#141414" stroke="#5F5E5A" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#D3D1C7" x="545" y="456" text-anchor="middle" dominant-baseline="central">Log anomaly</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#888780" x="545" y="474" text-anchor="middle" dominant-baseline="central">Save for review</text>
<!-- arrows to response boxes -->
<line x1="300" y1="434" x2="210" y2="434" stroke="#D85A30" stroke-width="1" marker-end="url(#a1)"/>
<line x1="415" y1="434" x2="465" y2="434" stroke="#888780" stroke-width="1" marker-end="url(#a1)"/>
</svg>
    </div>
  </div>

  <!-- FLOWCHART 2 -->
  <div class="fc-card">
    <div class="fc-header">
      <span class="fc-num">02</span>
      <div><div class="fc-title">Multi-signal threat detection</div><div class="fc-sub">4 signals → aggregator → ML → response</div></div>
    </div>
    <div class="fc-body">
<svg viewBox="0 0 680 560" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="a2" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<!-- Entry -->
<rect x="240" y="30" width="200" height="44" rx="8" fill="#141414" stroke="#5F5E5A" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#D3D1C7" x="340" y="52" text-anchor="middle" dominant-baseline="central">Device observed</text>
<!-- branch lines -->
<line x1="340" y1="74" x2="340" y2="104" stroke="#5F5E5A" stroke-width="1"/>
<line x1="80" y1="104" x2="600" y2="104" stroke="#5F5E5A" stroke-width="0.5"/>
<line x1="80" y1="104" x2="80" y2="122" stroke="#BA7517" stroke-width="1" marker-end="url(#a2)"/>
<line x1="247" y1="104" x2="247" y2="122" stroke="#BA7517" stroke-width="1" marker-end="url(#a2)"/>
<line x1="433" y1="104" x2="433" y2="122" stroke="#BA7517" stroke-width="1" marker-end="url(#a2)"/>
<line x1="600" y1="104" x2="600" y2="122" stroke="#BA7517" stroke-width="1" marker-end="url(#a2)"/>
<!-- 4 signal boxes -->
<rect x="28" y="122" width="104" height="56" rx="8" fill="#25190a" stroke="#854F0B" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="13" font-weight="500" fill="#EF9F27" x="80" y="144" text-anchor="middle" dominant-baseline="central">PPS spike?</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#BA7517" x="80" y="162" text-anchor="middle" dominant-baseline="central">vs. baseline</text>
<rect x="195" y="122" width="104" height="56" rx="8" fill="#25190a" stroke="#854F0B" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="13" font-weight="500" fill="#EF9F27" x="247" y="144" text-anchor="middle" dominant-baseline="central">Promisc mode?</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#BA7517" x="247" y="162" text-anchor="middle" dominant-baseline="central">NIC flag</text>
<rect x="381" y="122" width="104" height="56" rx="8" fill="#25190a" stroke="#854F0B" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="13" font-weight="500" fill="#EF9F27" x="433" y="140" text-anchor="middle" dominant-baseline="central">IP–MAC</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#BA7517" x="433" y="158" text-anchor="middle" dominant-baseline="central">mismatch?</text>
<rect x="548" y="122" width="104" height="56" rx="8" fill="#25190a" stroke="#854F0B" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="13" font-weight="500" fill="#EF9F27" x="600" y="140" text-anchor="middle" dominant-baseline="central">Bad device?</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#BA7517" x="600" y="158" text-anchor="middle" dominant-baseline="central">Vendor/MAC</text>
<!-- signal labels -->
<text font-family="Barlow,sans-serif" font-size="11" fill="#BA7517" x="80" y="196">+1 signal</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#BA7517" x="230" y="196">+1 signal</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#BA7517" x="416" y="196">+1 signal</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#BA7517" x="582" y="196">+1 signal</text>
<!-- arrows to aggregator -->
<line x1="80" y1="178" x2="80" y2="216" stroke="#BA7517" stroke-width="1"/>
<line x1="247" y1="178" x2="247" y2="216" stroke="#BA7517" stroke-width="1"/>
<line x1="433" y1="178" x2="433" y2="216" stroke="#BA7517" stroke-width="1"/>
<line x1="600" y1="178" x2="600" y2="216" stroke="#BA7517" stroke-width="1"/>
<line x1="80" y1="216" x2="600" y2="216" stroke="#BA7517" stroke-width="0.5"/>
<line x1="340" y1="216" x2="340" y2="236" stroke="#BA7517" stroke-width="1" marker-end="url(#a2)"/>
<!-- Aggregator -->
<rect x="200" y="236" width="280" height="52" rx="8" fill="#1a0d38" stroke="#534AB7" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#AFA9EC" x="340" y="258" text-anchor="middle" dominant-baseline="central">Signal aggregator</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#7F77DD" x="340" y="276" text-anchor="middle" dominant-baseline="central">Count confirmed indicators</text>
<line x1="340" y1="288" x2="340" y2="326" stroke="#7F77DD" stroke-width="1" marker-end="url(#a2)"/>
<!-- Decision -->
<polygon points="340,326 420,362 340,398 260,362" fill="#0a0e1a" stroke="#534AB7" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="13" font-weight="500" fill="#AFA9EC" x="340" y="358" text-anchor="middle" dominant-baseline="central">Signals ≥ 2?</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#7F77DD" x="340" y="374" text-anchor="middle" dominant-baseline="central">multi-confirm rule</text>
<!-- NO -->
<line x1="260" y1="362" x2="100" y2="362" stroke="#5F5E5A" stroke-width="1" marker-end="url(#a2)"/>
<text font-family="Barlow,sans-serif" font-size="11" fill="#888780" x="175" y="354">no</text>
<rect x="30" y="338" width="70" height="48" rx="8" fill="#0f1a10" stroke="#3B6D11" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#97C459" x="65" y="362" text-anchor="middle" dominant-baseline="central">Clear</text>
<!-- YES -->
<line x1="340" y1="398" x2="340" y2="436" stroke="#D85A30" stroke-width="1" marker-end="url(#a2)"/>
<text font-family="Barlow,sans-serif" font-size="11" fill="#D85A30" x="350" y="422">yes</text>
<!-- ML confirm -->
<rect x="200" y="436" width="280" height="52" rx="8" fill="#1a0d38" stroke="#534AB7" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#AFA9EC" x="340" y="458" text-anchor="middle" dominant-baseline="central">Isolation Forest confirms</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#7F77DD" x="340" y="476" text-anchor="middle" dominant-baseline="central">Outlier vs. learned baseline</text>
<line x1="340" y1="488" x2="340" y2="516" stroke="#D85A30" stroke-width="1" marker-end="url(#a2)"/>
<rect x="210" y="516" width="260" height="36" rx="8" fill="#250d05" stroke="#993C1D" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#F0997B" x="340" y="534" text-anchor="middle" dominant-baseline="central">Trigger response engine</text>
</svg>
    </div>
  </div>

  <!-- FLOWCHART 3 -->
  <div class="fc-card">
    <div class="fc-header">
      <span class="fc-num">03</span>
      <div><div class="fc-title">Automated response engine</div><div class="fc-sub">3 parallel actions fire on threat confirmation</div></div>
    </div>
    <div class="fc-body">
<svg viewBox="0 0 680 420" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="a3" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<!-- Trigger -->
<rect x="200" y="30" width="280" height="52" rx="8" fill="#250d05" stroke="#993C1D" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#F0997B" x="340" y="52" text-anchor="middle" dominant-baseline="central">Threat confirmed</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#D85A30" x="340" y="70" text-anchor="middle" dominant-baseline="central">Score exceeds threshold</text>
<line x1="340" y1="82" x2="340" y2="110" stroke="#D85A30" stroke-width="1"/>
<!-- parallel split -->
<line x1="140" y1="110" x2="540" y2="110" stroke="#5F5E5A" stroke-width="0.5"/>
<line x1="140" y1="110" x2="140" y2="140" stroke="#D85A30" stroke-width="1" marker-end="url(#a3)"/>
<line x1="340" y1="110" x2="340" y2="140" stroke="#EF9F27" stroke-width="1" marker-end="url(#a3)"/>
<line x1="540" y1="110" x2="540" y2="140" stroke="#5F5E5A" stroke-width="1" marker-end="url(#a3)"/>
<!-- 3 action boxes -->
<rect x="50" y="140" width="180" height="90" rx="8" fill="#250d05" stroke="#993C1D" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#F0997B" x="140" y="168" text-anchor="middle" dominant-baseline="central">Block device</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#D85A30" x="140" y="186" text-anchor="middle" dominant-baseline="central">Isolate from network</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#993C1D" x="140" y="204" text-anchor="middle" dominant-baseline="central">No manual step</text>
<rect x="250" y="140" width="180" height="90" rx="8" fill="#25190a" stroke="#854F0B" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#EF9F27" x="340" y="168" text-anchor="middle" dominant-baseline="central">Email alert</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#BA7517" x="340" y="186" text-anchor="middle" dominant-baseline="central">Device + threat details</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#854F0B" x="340" y="204" text-anchor="middle" dominant-baseline="central">Delivered to admin</text>
<rect x="450" y="140" width="180" height="90" rx="8" fill="#141414" stroke="#5F5E5A" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#D3D1C7" x="540" y="168" text-anchor="middle" dominant-baseline="central">Log anomaly</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#888780" x="540" y="186" text-anchor="middle" dominant-baseline="central">Timestamp + signals</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#5F5E5A" x="540" y="204" text-anchor="middle" dominant-baseline="central">Saved for review</text>
<!-- merge -->
<line x1="140" y1="230" x2="140" y2="286" stroke="#D85A30" stroke-width="1"/>
<line x1="340" y1="230" x2="340" y2="286" stroke="#EF9F27" stroke-width="1"/>
<line x1="540" y1="230" x2="540" y2="286" stroke="#5F5E5A" stroke-width="1"/>
<line x1="140" y1="286" x2="540" y2="286" stroke="#5F5E5A" stroke-width="0.5"/>
<line x1="340" y1="286" x2="340" y2="316" stroke="#1D9E75" stroke-width="1" marker-end="url(#a3)"/>
<!-- Resume -->
<rect x="190" y="316" width="300" height="52" rx="8" fill="#041a12" stroke="#0F6E56" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#5DCAA5" x="340" y="338" text-anchor="middle" dominant-baseline="central">Resume monitoring</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#1D9E75" x="340" y="356" text-anchor="middle" dominant-baseline="central">System keeps watching network</text>
</svg>
    </div>
  </div>

  <!-- FLOWCHART 4 -->
  <div class="fc-card">
    <div class="fc-header">
      <span class="fc-num">04</span>
      <div><div class="fc-title">Data pipeline</div><div class="fc-sub">Raw packets → JSON → features → ML → decision</div></div>
    </div>
    <div class="fc-body">
<svg viewBox="0 0 680 200" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="a4" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<rect x="20" y="56" width="108" height="80" rx="8" fill="#0d1f38" stroke="#185FA5" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="13" font-weight="500" fill="#85B7EB" x="74" y="82" text-anchor="middle" dominant-baseline="central">Raw packets</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#378ADD" x="74" y="100" text-anchor="middle" dominant-baseline="central">TShark</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#185FA5" x="74" y="118" text-anchor="middle" dominant-baseline="central">live stream</text>
<line x1="128" y1="96" x2="152" y2="96" stroke="#378ADD" stroke-width="1" marker-end="url(#a4)"/>
<rect x="152" y="56" width="108" height="80" rx="8" fill="#0d1f38" stroke="#185FA5" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="13" font-weight="500" fill="#85B7EB" x="206" y="82" text-anchor="middle" dominant-baseline="central">JSON parser</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#378ADD" x="206" y="100" text-anchor="middle" dominant-baseline="central">Structured</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#185FA5" x="206" y="118" text-anchor="middle" dominant-baseline="central">per-device</text>
<line x1="260" y1="96" x2="284" y2="96" stroke="#7F77DD" stroke-width="1" marker-end="url(#a4)"/>
<rect x="284" y="56" width="112" height="80" rx="8" fill="#1a0d38" stroke="#534AB7" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="13" font-weight="500" fill="#AFA9EC" x="340" y="78" text-anchor="middle" dominant-baseline="central">Feature eng.</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#7F77DD" x="340" y="96" text-anchor="middle" dominant-baseline="central">PPS, promisc</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#534AB7" x="340" y="114" text-anchor="middle" dominant-baseline="central">IP-MAC delta</text>
<line x1="396" y1="96" x2="420" y2="96" stroke="#7F77DD" stroke-width="1" marker-end="url(#a4)"/>
<rect x="420" y="56" width="108" height="80" rx="8" fill="#1a0d38" stroke="#534AB7" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="13" font-weight="500" fill="#AFA9EC" x="474" y="78" text-anchor="middle" dominant-baseline="central">Iso Forest</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#7F77DD" x="474" y="96" text-anchor="middle" dominant-baseline="central">Scores anomaly</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#534AB7" x="474" y="114" text-anchor="middle" dominant-baseline="central">vs. baseline</text>
<line x1="528" y1="96" x2="552" y2="96" stroke="#D85A30" stroke-width="1" marker-end="url(#a4)"/>
<rect x="552" y="56" width="108" height="80" rx="8" fill="#250d05" stroke="#993C1D" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="13" font-weight="500" fill="#F0997B" x="606" y="78" text-anchor="middle" dominant-baseline="central">Decision</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#D85A30" x="606" y="96" text-anchor="middle" dominant-baseline="central">threat /</text>
<text font-family="Barlow,sans-serif" font-size="11" fill="#993C1D" x="606" y="114" text-anchor="middle" dominant-baseline="central">clear</text>
</svg>
    </div>
  </div>

  <!-- FLOWCHART 5 -->
  <div class="fc-card">
    <div class="fc-header">
      <span class="fc-num">05</span>
      <div><div class="fc-title">False positive prevention</div><div class="fc-sub">How each signal gets validated before triggering a block</div></div>
    </div>
    <div class="fc-body">
<svg viewBox="0 0 680 470" xmlns="http://www.w3.org/2000/svg">
<defs><marker id="a5" viewBox="0 0 10 10" refX="8" refY="5" markerWidth="6" markerHeight="6" orient="auto-start-reverse"><path d="M2 1L8 5L2 9" fill="none" stroke="context-stroke" stroke-width="1.5" stroke-linecap="round" stroke-linejoin="round"/></marker></defs>
<!-- Start -->
<rect x="230" y="28" width="220" height="44" rx="8" fill="#141414" stroke="#5F5E5A" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#D3D1C7" x="340" y="50" text-anchor="middle" dominant-baseline="central">Signal detected</text>
<line x1="340" y1="72" x2="340" y2="104" stroke="#5F5E5A" stroke-width="1" marker-end="url(#a5)"/>
<!-- Check 1 -->
<rect x="160" y="104" width="320" height="56" rx="8" fill="#25190a" stroke="#854F0B" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#EF9F27" x="320" y="126" text-anchor="middle" dominant-baseline="central">Check 1 — PPS spike</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#BA7517" x="320" y="144" text-anchor="middle" dominant-baseline="central">vs. rolling average, not fixed cutoff</text>
<line x1="480" y1="132" x2="554" y2="132" stroke="#3B6D11" stroke-width="1" marker-end="url(#a5)"/>
<text font-family="Barlow,sans-serif" font-size="11" fill="#639922" x="514" y="124">within normal</text>
<rect x="554" y="108" width="80" height="48" rx="8" fill="#0f1a10" stroke="#3B6D11" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#97C459" x="594" y="132" text-anchor="middle" dominant-baseline="central">Pass</text>
<line x1="340" y1="160" x2="340" y2="192" stroke="#EF9F27" stroke-width="1" marker-end="url(#a5)"/>
<!-- Check 2 -->
<rect x="140" y="192" width="360" height="56" rx="8" fill="#25190a" stroke="#854F0B" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#EF9F27" x="320" y="214" text-anchor="middle" dominant-baseline="central">Check 2 — Promiscuous mode</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#BA7517" x="320" y="232" text-anchor="middle" dominant-baseline="central">Only flag if traffic anomaly also present</text>
<line x1="500" y1="220" x2="554" y2="220" stroke="#3B6D11" stroke-width="1" marker-end="url(#a5)"/>
<text font-family="Barlow,sans-serif" font-size="11" fill="#639922" x="504" y="212">mode only</text>
<rect x="554" y="196" width="80" height="48" rx="8" fill="#0f1a10" stroke="#3B6D11" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#97C459" x="594" y="220" text-anchor="middle" dominant-baseline="central">Pass</text>
<line x1="340" y1="248" x2="340" y2="280" stroke="#EF9F27" stroke-width="1" marker-end="url(#a5)"/>
<!-- Check 3 -->
<rect x="140" y="280" width="360" height="56" rx="8" fill="#25190a" stroke="#854F0B" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#EF9F27" x="320" y="302" text-anchor="middle" dominant-baseline="central">Check 3 — IP–MAC mismatch</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#BA7517" x="320" y="320" text-anchor="middle" dominant-baseline="central">Persistent over multiple scans</text>
<line x1="500" y1="308" x2="554" y2="308" stroke="#3B6D11" stroke-width="1" marker-end="url(#a5)"/>
<text font-family="Barlow,sans-serif" font-size="11" fill="#639922" x="504" y="300">one-off only</text>
<rect x="554" y="284" width="80" height="48" rx="8" fill="#0f1a10" stroke="#3B6D11" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#97C459" x="594" y="308" text-anchor="middle" dominant-baseline="central">Pass</text>
<line x1="340" y1="336" x2="340" y2="368" stroke="#EF9F27" stroke-width="1" marker-end="url(#a5)"/>
<!-- Multi-signal gate -->
<rect x="160" y="368" width="360" height="56" rx="8" fill="#1a0d38" stroke="#534AB7" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="14" font-weight="500" fill="#AFA9EC" x="340" y="390" text-anchor="middle" dominant-baseline="central">Multi-signal gate</text>
<text font-family="Barlow,sans-serif" font-size="12" fill="#7F77DD" x="340" y="408" text-anchor="middle" dominant-baseline="central">≥ 2 checks triggered → threat confirmed</text>
<line x1="340" y1="424" x2="340" y2="450" stroke="#D85A30" stroke-width="1" marker-end="url(#a5)"/>
<rect x="240" y="450" width="200" height="16" rx="6" fill="#250d05" stroke="#993C1D" stroke-width="0.5"/>
<text font-family="Barlow,sans-serif" font-size="11" font-weight="500" fill="#F0997B" x="340" y="458" text-anchor="middle" dominant-baseline="central">Response engine</text>
</svg>
    </div>
  </div>
</div>

<hr class="divider">

<!-- ═══════════════════════════════ TOOLS ════════════════════════════════ -->
<div class="section">
  <div class="section-label">// 03 — Tech Stack</div>
  <div class="section-title">Tools & technologies</div>
  <table class="tools-table">
    <tr><th>Category</th><th>Tool</th><th>Purpose</th></tr>
    <tr><td class="tool-cat">Network scanning</td><td class="tool-name">Nmap</td><td class="tool-desc">Discovers all devices — IP, MAC, vendor, open ports, state</td></tr>
    <tr><td class="tool-cat">Packet capture</td><td class="tool-name">TShark</td><td class="tool-desc">CLI Wireshark — captures live per-device traffic and extracts metrics</td></tr>
    <tr><td class="tool-cat">Backend</td><td class="tool-name">Python 3.8+</td><td class="tool-desc">Core orchestration, signal processing, response logic</td></tr>
    <tr><td class="tool-cat">ML model</td><td class="tool-name">Isolation Forest</td><td class="tool-desc">Unsupervised anomaly detection against learned device baselines</td></tr>
    <tr><td class="tool-cat">Data pipeline</td><td class="tool-name">JSON + Pandas</td><td class="tool-desc">Structures raw packet capture into ML-ready feature vectors</td></tr>
    <tr><td class="tool-cat">Feature engineering</td><td class="tool-name">NumPy</td><td class="tool-desc">PPS calculation, rolling averages, delta tracking per device</td></tr>
    <tr><td class="tool-cat">Alerting</td><td class="tool-name">SMTP (smtplib)</td><td class="tool-desc">Real-time email alerts sent to the network admin on threat detection</td></tr>
    <tr><td class="tool-cat">Blocking</td><td class="tool-name">iptables / netsh</td><td class="tool-desc">Auto-blocks flagged device at the OS network layer instantly</td></tr>
    <tr><td class="tool-cat">Logging</td><td class="tool-name">Python logging</td><td class="tool-desc">Structured anomaly logs with timestamps, signals, and scores</td></tr>
  </table>
</div>

<hr class="divider">

<!-- ═══════════════════════════════ COMPARISON ══════════════════════════ -->
<div class="section">
  <div class="section-label">// 04 — Why This Is Different</div>
  <div class="section-title">Smart Gateway vs. the rest</div>
  <table class="cmp-table">
    <tr><th>Feature</th><th>Nmap</th><th>Wireshark</th><th>Smart Gateway</th></tr>
    <tr><td>Device discovery</td><td class="yes">✓</td><td class="no">✗</td><td class="sg">✓</td></tr>
    <tr><td>Live traffic capture</td><td class="no">✗</td><td class="yes">✓</td><td class="sg">✓</td></tr>
    <tr><td>Real-time analysis</td><td class="no">✗</td><td class="no">✗</td><td class="sg">✓</td></tr>
    <tr><td>Behavior-based ML detection</td><td class="no">✗</td><td class="no">✗</td><td class="sg">✓</td></tr>
    <tr><td>Automatic device blocking</td><td class="no">✗</td><td class="no">✗</td><td class="sg">✓</td></tr>
    <tr><td>Admin email alerts</td><td class="no">✗</td><td class="no">✗</td><td class="sg">✓</td></tr>
    <tr><td>Requires human to act</td><td class="yes">✓</td><td class="yes">✓</td><td class="sgno">✗</td></tr>
  </table>
</div>

<!-- ═══════════════════════════════ DEEP DIVE ═══════════════════════════ -->
<div class="section">
  <div class="section-label">// 05 — Detection Deep Dive</div>
  <div class="section-title">How the signals work</div>
  <div class="deep-grid">
    <div class="deep-card">
      <div class="deep-title">Adaptive PPS Threshold</div>
      <p>Rather than a fixed cutoff, the system maintains a rolling baseline per device. A spike has to be meaningfully above <em>that device's</em> normal — not some global number.</p>
    </div>
    <div class="deep-card">
      <div class="deep-title">Promiscuous Mode</div>
      <p>A strong MITM/sniffing indicator, but VMs and some adapters can false-positive. Smart Gateway uses it as a <em>supporting signal only</em> — it confirms, never accuses alone.</p>
    </div>
    <div class="deep-card">
      <div class="deep-title">IP–MAC Consistency</div>
      <p>Spoofing attacks often recycle IPs with forged MACs. The system tracks mappings over time and flags persistent inconsistencies, not one-off DHCP quirks.</p>
    </div>
    <div class="deep-card">
      <div class="deep-title">Device Integrity</div>
      <p>Unknown OUI vendor, duplicate MAC, or mismatched identity across scans? Any of these alone is suspicious. Multiple together triggers a block.</p>
    </div>
  </div>
</div>

<hr class="divider">

<!-- ═══════════════════════════════ CHALLENGES ══════════════════════════ -->
<div class="section">
  <div class="section-label">// 06 — Challenges We Solved</div>
  <div class="section-title">Hard problems, real solutions</div>
  <div class="challenge-list">
    <div class="challenge-item">
      <div class="ch-num">01</div>
      <div class="ch-body">
        <div class="ch-title">Real threats vs. normal traffic spikes</div>
        <p>Sudden PPS spikes also happen during legitimate usage. Solved with adaptive thresholds based on rolling average PPS. Multiple signals must align before any alert fires.</p>
      </div>
    </div>
    <div class="challenge-item">
      <div class="ch-num">02</div>
      <div class="ch-body">
        <div class="ch-title">Promiscuous mode false positives</div>
        <p>VMs and certain adapters trigger promiscuous mode without malicious intent. Made it a supporting signal only — confirmed alongside traffic anomalies before action.</p>
      </div>
    </div>
    <div class="challenge-item">
      <div class="ch-num">03</div>
      <div class="ch-body">
        <div class="ch-title">Accurate spoofing detection</div>
        <p>IP-MAC mismatches can be noisy in dynamic DHCP environments. Consistency verified over time, cross-referenced against network activity patterns before flagging.</p>
      </div>
    </div>
  </div>
</div>

<hr class="divider">

<!-- ═══════════════════════════════ MISC ════════════════════════════════ -->
<div class="section">
  <div class="section-label">// 07 — Disclaimer</div>
  <div class="section-title">Authorized use only</div>
  <p class="prose">Smart Gateway is built for <strong>authorized network environments only</strong>. Only deploy on networks you own or have explicit permission to monitor. Unauthorized network scanning and traffic analysis is illegal in most jurisdictions.</p>
</div>

<div class="bottom-row">
  <div class="bottom-card">
    <div class="bottom-icon">🤝</div>
    <div class="bottom-label">Contributing</div>
    <p>PRs welcome. If you find a false positive pattern we haven't handled, open an issue — that's genuinely valuable data.</p>
  </div>
  <div class="bottom-card">
    <div class="bottom-icon">📄</div>
    <div class="bottom-label">License</div>
    <p>MIT License — use it, build on it, just don't be evil with it.</p>
  </div>
</div>

<hr class="divider">

<!-- ═══════════════════════════════ FOOTER ══════════════════════════════ -->
<div class="footer">
  <p>Built at a hackathon. Designed to actually work.</p>
  <p class="highlight">We're not just detecting attacks — we're stopping them as they happen.</p>
  <p style="margin-top:16px">
    <span style="color:#FF9933">●</span>
    <span style="color:#ffffff"> Smart Gateway </span>
    <span style="color:#138808">●</span>
    <span style="color:#000080"> ☸ </span>
    <span style="color:#FF9933">●</span>
    <span style="color:#ffffff"> Jai Hind </span>
    <span style="color:#138808">●</span>
  </p>
</div>

</div>
</body>
</html>
