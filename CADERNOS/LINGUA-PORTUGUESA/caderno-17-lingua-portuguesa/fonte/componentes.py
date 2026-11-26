"""Componentes visuais reutilizáveis dos Cadernos Simplificados (ícones, personagens, boxes, fluxos)."""
import html as _h

C = dict(navy="#2a1745", blue="#6b3fa0", sky="#f2ebfa", sky2="#dccbf0", gold="#f5c518", golddeep="#8a6200",
         goldsoft="#fff3c4", cream="#f7f0e1", red="#d6332a", redsoft="#fdecea", green="#2c8a5a",
         greensoft="#e4f4ec", ink="#16202f", muted="#5a6476")

# ---------------- ícones (viewBox 24, traço = currentColor) ----------------
S = 'fill="none" stroke="currentColor" stroke-width="1.8" stroke-linecap="round" stroke-linejoin="round"'
ICONS = {
 "monitor": f'<path {S} d="M3 4h18v12H3zM8 20h8M12 16v4"/>',
 "cpu": f'<g {S}><rect x="6" y="6" width="12" height="12" rx="1.5"/><rect x="9.5" y="9.5" width="5" height="5"/><path d="M9 3v3M15 3v3M9 18v3M15 18v3M3 9h3M3 15h3M18 9h3M18 15h3"/></g>',
 "wifi": f'<g {S}><path d="M2.5 9a14 14 0 0 1 19 0M5.5 12.5a9.5 9.5 0 0 1 13 0M8.5 16a5 5 0 0 1 7 0"/><circle cx="12" cy="19.2" r=".8"/></g>',
 "cloud": f'<path {S} d="M7 18h10.5a4 4 0 0 0 .6-7.95A6 6 0 0 0 6.6 9.1 4.5 4.5 0 0 0 7 18z"/>',
 "bug": f'<g {S}><rect x="7.5" y="8" width="9" height="12" rx="4.5"/><path d="M9 8a3 3 0 0 1 6 0M12 12v8M3.5 10.5l4 1.5M20.5 10.5l-4 1.5M3.5 17l4-1.5M20.5 17l-4-1.5M3 13.8h4.5M16.5 13.8H21"/></g>',
 "folder": f'<path {S} d="M3 6.5h6l2 2.5h10v10H3z"/>',
 "keyboard": f'<g {S}><rect x="2.5" y="6" width="19" height="12" rx="2"/><path d="M6 10h.01M9 10h.01M12 10h.01M15 10h.01M18 10h.01M7 14h10"/></g>',
 "printer": f'<path {S} d="M7 9V3h10v6M6 17H4v-7h16v7h-2M7 14h10v7H7z"/>',
 "book": f'<path {S} d="M3 5c3-1.5 6-1.5 9 0v15c-3-1.5-6-1.5-9 0zM21 5c-3-1.5-6-1.5-9 0v15c3-1.5 6-1.5 9 0z"/>',
 "scroll": f'<path {S} d="M6 4h11a2 2 0 0 1 2 2v12H8a2 2 0 0 1-2-2zM6 4a2 2 0 0 0-2 2v2h2M8 18a2 2 0 0 0 2 2h9a2 2 0 0 0 2-2v-1H10M9.5 8h6M9.5 11h6M9.5 14h4"/>',
 "pyramid": f'<path {S} d="M12 3 2.5 20h19zM7.5 11.3h9M5 15.7h14"/>',
 "people": f'<g {S}><circle cx="8" cy="8" r="3"/><circle cx="16.5" cy="9" r="2.4"/><path d="M2.5 20c.5-4 3-6 5.5-6s5 2 5.5 6M13.5 15c1-1.3 2-2 3-2 2.2 0 4 1.8 4.5 5"/></g>',
 "person": f'<g {S}><circle cx="12" cy="7" r="3.5"/><path d="M5 21c.6-4.5 3.4-7 7-7s6.4 2.5 7 7"/></g>',
 "flag": f'<path {S} d="M5 21V4M5 4h11l-2 3.5L16 11H5"/>',
 "globe": f'<g {S}><circle cx="12" cy="12" r="9"/><path d="M3 12h18M12 3c2.5 2.7 3.8 5.7 3.8 9s-1.3 6.3-3.8 9c-2.5-2.7-3.8-5.7-3.8-9S9.5 5.7 12 3z"/></g>',
 "handshake": f'<path {S} d="M2 11l4-4 4 2 3-2 3 1 6 4M2 11l5 5 2-1 2 2 2-1 2 2 3-3 4-4M9 9l-2 3a1.5 1.5 0 0 0 2.5 1.6L12 11"/>',
 "dove": f'<path {S} d="M3 14c3 0 5-1 7-4 1.5-2.2 3-3 5-3l3-2-.6 3.2C19 9.5 18.5 13 15 15c-2 1.2-4.5 1.5-7 1L5 19l1-3.5C4.5 15 3.5 14.7 3 14zM15 7h.01"/>',
 "scales": f'<g {S}><path d="M12 3v17M7 20.5h10M4 7h16"/><path d="M6.5 7 3.5 13.5a3 3 0 0 0 6 0zM17.5 7l-3 6.5a3 3 0 0 0 6 0z"/></g>',
 "gavel": f'<path {S} d="M14 4l6 6M11 7l6 6M12.5 5.5l-4 4 6 6 4-4M10.5 11.5 4 18a1.4 1.4 0 0 0 2 2l6.5-6.5M3 21h8"/>',
 "capitol": f'<path {S} d="M3 21h18M5 21v-8M9.5 21v-8M14.5 21v-8M19 21v-8M3.5 13h17M6 10.5a6 6 0 0 1 12 0zM12 4.5V3"/>',
 "house": f'<path {S} d="M3 11 12 4l9 7M5.5 9.5V20h13V9.5M10 20v-5h4v5"/>',
 "city": f'<path {S} d="M3 21h18M4.5 21V9l5-3v15M9.5 21V4l6 3v14M15.5 21v-9l4 2v7M12 9h1M12 12h1M12 15h1M6.5 12h1M6.5 15h1"/>',
 "map": f'<path {S} d="M9 4 3 6.5v13.5l6-2.5 6 2.5 6-2.5V4l-6 2.5zM9 4v13.5M15 6.5V20"/>',
 "crown": f'<path {S} d="M3 8l4 4 5-7 5 7 4-4-2 11H5zM5 21h14"/>',
 "ballot": f'<path {S} d="M4 13h16v8H4zM8 13V6l6-3 2.5 5L10 13M8.5 17h7"/>',
 "shield": f'<path {S} d="M12 3 4 6v6c0 4.5 3.4 8 8 9 4.6-1 8-4.5 8-9V6zM8.5 12l2.5 2.5 4.5-5"/>',
 "star": f'<path {S} d="M12 3l2.7 5.6 6.1.9-4.4 4.3 1 6.1L12 17l-5.4 2.9 1-6.1L3.2 9.5l6.1-.9z"/>',
 "key": f'<g {S}><circle cx="7.5" cy="12" r="4"/><path d="M11.5 12H21M17 12v3.5M20 12v2.5"/></g>',
 "target": f'<g {S}><circle cx="12" cy="12" r="9"/><circle cx="12" cy="12" r="5"/><circle cx="12" cy="12" r="1.3"/></g>',
 "chain": f'<path {S} d="M10 14a4 4 0 0 0 5.7 0l3-3a4 4 0 0 0-5.7-5.7l-1 1M14 10a4 4 0 0 0-5.7 0l-3 3a4 4 0 0 0 5.7 5.7l1-1"/>',
 "briefcase": f'<path {S} d="M3 8h18v12H3zM8.5 8V5h7v3M3 13h18M11 13v2h2v-2"/>',
 "heart": f'<path {S} d="M12 20s-7.5-4.6-9-9.3C2 7.4 4.3 4.5 7.4 4.5c2 0 3.6 1.1 4.6 2.7 1-1.6 2.6-2.7 4.6-2.7 3.1 0 5.4 2.9 4.4 6.2C19.5 15.4 12 20 12 20z"/>',
 "idcard": f'<g {S}><rect x="3" y="5" width="18" height="14" rx="2"/><circle cx="8.5" cy="11" r="2.2"/><path d="M5.5 16c.6-1.7 1.7-2.5 3-2.5s2.4.8 3 2.5M14 10h4M14 13h3"/></g>',
 "puzzle": f'<path {S} d="M4 8h4a2 2 0 1 1 4 0h4v4a2 2 0 1 1 0 4v4h-4a2 2 0 1 0-4 0H4v-4a2 2 0 1 0 0-4z"/>',
 "bulb": f'<path {S} d="M9 17h6M10 20.5h4M12 2.5a6.5 6.5 0 0 0-3.8 11.8c.6.5.8 1.1.8 1.7h6c0-.6.2-1.2.8-1.7A6.5 6.5 0 0 0 12 2.5z"/>',
 "alert": f'<g {S}><path d="M12 3 2 20.5h20z"/><path d="M12 9.5v5M12 17.5h.01"/></g>',
 "check": f'<g {S}><circle cx="12" cy="12" r="9"/><path d="M8 12.5l2.7 2.7L16 9.5"/></g>',
 "xmark": f'<g {S}><circle cx="12" cy="12" r="9"/><path d="M9 9l6 6M15 9l-6 6"/></g>',
 "pen": f'<path {S} d="M4 20l1-4L16 5l3 3L8 19zM14 7l3 3M4 20h6"/>',
 "calendar": f'<g {S}><rect x="3.5" y="5" width="17" height="15" rx="2"/><path d="M3.5 10h17M8 3v4M16 3v4"/></g>',
 "lock": f'<g {S}><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 8 0v3M12 15v2"/></g>',
 "chart": f'<path {S} d="M4 20V4M4 20h16M7.5 15l4-4 3 3 5-6M16 8h3.5v3.5"/>',
 "stop": f'<g {S}><path d="M8 3h8l5 5v8l-5 5H8l-5-5V8z"/><path d="M8.5 12h7"/></g>',
 "umbrella": f'<path {S} d="M3 12a9 9 0 0 1 18 0zM12 12v6.5a2 2 0 0 1-4 0M12 3v.5"/>',
 "q": f'<g {S}><circle cx="12" cy="12" r="9.5"/><path d="M9.3 9.3a2.8 2.8 0 1 1 3.9 2.6c-.8.4-1.2 1-1.2 1.9v.6M12 17.3h.01"/></g>',
 "pin": f'<g {S}><path d="M12 21s-6.5-6.2-6.5-11a6.5 6.5 0 0 1 13 0C18.5 14.8 12 21 12 21z"/><circle cx="12" cy="10" r="2.3"/></g>',
 "layers": f'<path {S} d="M12 3 2.5 8 12 13l9.5-5zM2.5 12.5 12 17.5l9.5-5M2.5 16.5 12 21.5l9.5-5"/>',
 "link": f'<path {S} d="M4 12h16M15 7l5 5-5 5"/>',
 "grid": f'<g {S}><rect x="3" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="3" width="7.5" height="7.5" rx="1.5"/><rect x="3" y="13.5" width="7.5" height="7.5" rx="1.5"/><rect x="13.5" y="13.5" width="7.5" height="7.5" rx="1.5"/></g>',
 "split": f'<path {S} d="M12 3v6M12 9l-7 6v6M12 9l7 6v6M5 21h0M19 21h0"/>',
 "fire": f'<path {S} d="M12 21c-4 0-6.5-2.7-6.5-6.3 0-3.7 3-5.7 3.8-9.2 1.7 1.2 2.6 3 2.7 4.8 1-1 1.6-2.3 1.6-3.8 2.5 2 4.9 5 4.9 8.4 0 3.5-2.5 6.1-6.5 6.1z"/>',
 "church": f'<path {S} d="M12 2v5M10 4h4M6 21V12l6-5 6 5v9M3 21h18M10 21v-4a2 2 0 0 1 4 0v4"/>',
 "doc": f'<path {S} d="M6 3h8l4 4v14H6zM14 3v4h4M9 12h6M9 15.5h6M9 9h3"/>',
 "envelope": f'<g {S}><rect x="3" y="5.5" width="18" height="13" rx="2"/><path d="M3.5 7 12 13l8.5-6"/></g>',
 "phone": f'<path {S} d="M6.5 3h3l1.5 4.5-2 1.5a12 12 0 0 0 6 6l1.5-2 4.5 1.5v3a2 2 0 0 1-2 2A17 17 0 0 1 4.5 5a2 2 0 0 1 2-2z"/>',
 "megaphone": f'<path {S} d="M3 10v4h3l7 5V5L6 10zM16 9a4 4 0 0 1 0 6M18.5 6.5a7.5 7.5 0 0 1 0 11"/>',
 "database": f'<g {S}><ellipse cx="12" cy="5.5" rx="7.5" ry="2.8"/><path d="M4.5 5.5v13c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8v-13M4.5 12c0 1.5 3.4 2.8 7.5 2.8s7.5-1.3 7.5-2.8"/></g>',
 "jail": f'<g {S}><rect x="3.5" y="3.5" width="17" height="17" rx="2"/><path d="M8 3.5v17M12 3.5v17M16 3.5v17"/></g>',
 "unlock": f'<g {S}><rect x="5" y="11" width="14" height="10" rx="2"/><path d="M8 11V8a4 4 0 0 1 7.6-1.7M12 15v2"/></g>',
 "sun": f'<g {S}><circle cx="12" cy="12" r="4"/><path d="M12 2.5v2M12 19.5v2M2.5 12h2M19.5 12h2M5.3 5.3l1.4 1.4M17.3 17.3l1.4 1.4M5.3 18.7l1.4-1.4M17.3 6.7l1.4-1.4"/></g>',
 "moon": f'<path {S} d="M20 14.5A8 8 0 1 1 9.5 4a6.5 6.5 0 0 0 10.5 10.5z"/>',
 "eye": f'<g {S}><path d="M2 12s3.6-6.5 10-6.5S22 12 22 12s-3.6 6.5-10 6.5S2 12 2 12z"/><circle cx="12" cy="12" r="3"/></g>',
 "mask": f'<path {S} d="M3 7c3-1.5 6-1.5 9 0 3-1.5 6-1.5 9 0v4c0 4-3.5 7-6.5 7-1.3 0-2-1-2.5-2-.5 1-1.2 2-2.5 2C6.5 18 3 15 3 11zM7 11h2.5M14.5 11H17"/>',
 "hourglass": f'<path {S} d="M6 3h12M6 21h12M7 3c0 5 10 5 10 9s-10 4-10 9M17 3c0 5-10 5-10 9s10 4 10 9"/>',
 "pulse": f'<path {S} d="M2 12h4l2.5-6 4 12 3-8 1.5 2H22"/>',
 "cross": f'<path {S} d="M9 3h6v6h6v6h-6v6H9v-6H3V9h6z"/>',
 "tree": f'<path {S} d="M12 21v-6M12 15l-6 0 3-4H7l5-7 5 7h-2l3 4z"/>',
 "coin": f'<g {S}><circle cx="12" cy="12" r="8.5"/><path d="M14.5 9.2c-.5-.9-1.5-1.4-2.6-1.4-1.5 0-2.6.8-2.6 2s1.1 1.7 2.7 2c1.6.3 2.7.9 2.7 2.1s-1.2 2-2.7 2c-1.2 0-2.3-.6-2.7-1.5M12 6.5v1.3M12 16.2v1.3"/></g>',
 "puzzlex": f'<path {S} d="M4 8h4a2 2 0 1 1 4 0h4v4a2 2 0 1 1 0 4v4h-4M4 8v12h5"/>',
 "clock": f'<g {S}><circle cx="12" cy="12" r="9"/><path d="M12 7v5l3.5 2"/></g>',
 "badge": f'<g {S}><rect x="5" y="3" width="14" height="18" rx="2"/><circle cx="12" cy="10" r="2.6"/><path d="M8.5 16c.6-1.6 2-2.4 3.5-2.4s2.9.8 3.5 2.4M10 3v2h4V3"/></g>',
 "teacher": f'<g {S}><rect x="9" y="3.5" width="12" height="9" rx="1"/><circle cx="5.5" cy="9" r="2.3"/><path d="M2 20c.3-3.5 1.6-5.5 3.5-5.5S8.7 16 9 20M8 14l4-3"/></g>',
 "sitemap": f'<g {S}><rect x="9" y="3" width="6" height="5" rx="1"/><rect x="2.5" y="16" width="6" height="5" rx="1"/><rect x="9" y="16" width="6" height="5" rx="1"/><rect x="15.5" y="16" width="6" height="5" rx="1"/><path d="M12 8v4M5.5 16v-4h13v4M12 12v4"/></g>',
 "car": f'<g {S}><path d="M3 16v-4l2-5h14l2 5v4zM3 16v2.5M21 16v2.5M5 12h14"/><circle cx="7.5" cy="16" r="1.6"/><circle cx="16.5" cy="16" r="1.6"/></g>',
 "exam": f'<g {S}><path d="M6 3h12v18H6z"/><path d="M9 8l1.2 1.2L12.5 7M9 13l1.2 1.2 2.3-2.2M14 8h1.5M14 13h1.5M9 17.5h6"/></g>',
 "trophy": f'<path {S} d="M8 4h8v5a4 4 0 0 1-8 0zM8 6H4.5a3 3 0 0 0 3.5 4M16 6h3.5a3 3 0 0 1-3.5 4M12 13v4M8.5 21h7M9.5 17h5"/>',
 "fireman": f'<path {S} d="M12 3c-3 0-5.5 2.2-6 5h12c-.5-2.8-3-5-6-5zM4 8h16M7 8v3a5 5 0 0 0 10 0V8M12 3v2M8 21v-3a4 4 0 0 1 8 0v3"/>',
 "road": f'<path {S} d="M8 3 4 21M16 3l4 18M12 4v3M12 10v3M12 16v3"/>',
 "train": f'<g {S}><rect x="5" y="3" width="14" height="13" rx="3"/><path d="M5 10h14M9 20l-2 2M15 20l2 2M8.5 13.5h.01M15.5 13.5h.01"/></g>',
 "plane": f'<path {S} d="M10.5 21l1.5-6 7 3V16l-7-5V5a1.5 1.5 0 0 0-3 0v6l-7 5v2l7-3 1.5 6"/>',
 "search": f'<g {S}><circle cx="10.5" cy="10.5" r="6.5"/><path d="M15.5 15.5 21 21"/></g>',
 "siren": f'<path {S} d="M7 18v-6a5 5 0 0 1 10 0v6M5 21h14v-3H5zM12 3v2M4.5 6l1.4 1.4M19.5 6l-1.4 1.4"/>',
 "anchor": f'<g {S}><circle cx="12" cy="5" r="2"/><path d="M12 7v14M5 13a7 7 0 0 0 14 0M8 11h8"/></g>',
 "knife": f'<path {S} d="M4 20 14 10l3 3L7 23zM14 10l5-7 2 2-4 8"/>',
 "skull": f'<g {S}><path d="M12 3a8 8 0 0 0-5 14v3h10v-3a8 8 0 0 0-5-14z"/><circle cx="9" cy="11" r="1.6"/><circle cx="15" cy="11" r="1.6"/><path d="M10 20v-2M14 20v-2"/></g>',
 "brain": f'<path {S} d="M9 4a3 3 0 0 0-3 3 3 3 0 0 0-2 5 3 3 0 0 0 2 5 3 3 0 0 0 3 3h0a3 3 0 0 0 3-3V7a3 3 0 0 0-3-3zM15 4a3 3 0 0 1 3 3 3 3 0 0 1 2 5 3 3 0 0 1-2 5 3 3 0 0 1-3 3h0a3 3 0 0 1-3-3"/>',
 "stairs": f'<path {S} d="M3 20h5v-5h5v-5h5V5h3"/>',
 "handcuffs": f'<g {S}><circle cx="7" cy="15" r="4"/><circle cx="17" cy="15" r="4"/><path d="M7 11V6a2 2 0 0 1 4 0M17 11V6a2 2 0 0 0-4 0M11 6h2"/></g>',
 "phonecrack": f'<g {S}><rect x="7" y="2.5" width="10" height="19" rx="2"/><path d="M10 6l3 3-2 2 3 3M11 18.5h2"/></g>',
 "wallet": f'<g {S}><path d="M4 7h14a2 2 0 0 1 2 2v9a2 2 0 0 1-2 2H4z"/><path d="M4 7V6a2 2 0 0 1 2-2h10v3M15 13h3"/></g>',
 "mask2": f'<g {S}><circle cx="12" cy="8" r="4.5"/><path d="M7.5 7h9M4 21c.8-4.5 4-7 8-7s7.2 2.5 8 7"/></g>',
 "speech": f'<path {S} d="M4 5h16v10H10l-4 4v-4H4zM8 9h8M8 12h5"/>',
 "pill": f'<g {S}><rect x="3" y="9" width="18" height="6" rx="3" transform="rotate(-35 12 12)"/><path d="M9.5 8.3l4.6 6.6"/></g>',
 "leaf": f'<path {S} d="M5 19c0-8 5-14 15-15-1 10-7 15-15 15zM5 19l7-7"/>',
 "gun": f'<path {S} d="M3 8h16l2 2v2H11l-1 2H8l-1 5H4l1-6-2-2zM14 12v2h-3"/>',
 "venus": f'<g {S}><circle cx="12" cy="9" r="5.5"/><path d="M12 14.5V21M9 18h6"/></g>',
 "bolt": f'<path {S} d="M13 2 4 14h7l-1 8 9-12h-7z"/>',
 "home2": f'<path {S} d="M3 11 12 4l9 7M5.5 9.5V20h13V9.5M10 20v-5h4v5"/>',
}

def symbols():
    out = ['<svg width="0" height="0" style="position:absolute"><defs>']
    for k, v in ICONS.items():
        out.append(f'<symbol id="i-{k}" viewBox="0 0 24 24">{v}</symbol>')
    out.append(CHAR_PROF); out.append(CHAR_PROFA)
    out.append('</defs></svg>')
    return "\n".join(out)

def icon(name, color=None, size=None):
    st = f' style="color:{color}"' if color else ''
    sz = f' width="{size}" height="{size}"' if size else ''
    return f'<svg{sz}{st}><use href="#i-{name}"/></svg>'

# ---------------- personagens (ilustrações próprias) ----------------
SKIN = "#f1c39b"
CHAR_PROF = f'''<symbol id="ch-prof" viewBox="0 0 100 170">
 <ellipse cx="50" cy="164" rx="28" ry="5" fill="#000" opacity=".13"/>
 <rect x="38" y="110" width="10" height="48" rx="3" fill="#2b3445"/><rect x="52" y="110" width="10" height="48" rx="3" fill="#2b3445"/>
 <ellipse cx="42" cy="159" rx="9" ry="4" fill="{C['ink']}"/><ellipse cx="59" cy="159" rx="9" ry="4" fill="{C['ink']}"/>
 <path d="M30 62 Q50 55 70 62 L74 116 H26 Z" fill="{C['navy']}"/>
 <path d="M43 59 L50 82 L57 59 Z" fill="#fff"/><path d="M48.6 63 h2.8 l1.8 15 -3.2 6 -3.2 -6z" fill="{C['gold']}"/>
 <path d="M43 59 L50 82 L46 88 L38 64 Z M57 59 L50 82 L54 88 L62 64Z" fill="#163e7d"/>
 <path d="M30 64 Q21 86 25 108 L32 108 Q30 88 36 71 Z" fill="{C['navy']}"/><circle cx="28.5" cy="110" r="5" fill="{SKIN}"/>
 <path d="M67 63 L86 40 L92 45 L73 72 Z" fill="{C['navy']}"/><circle cx="89.5" cy="41" r="5.2" fill="{SKIN}"/>
 <rect x="88" y="27" width="3.4" height="11" rx="1.7" fill="{SKIN}"/>
 <rect x="45.5" y="48" width="9" height="11" rx="3" fill="{SKIN}"/>
 <circle cx="50" cy="35" r="16" fill="{SKIN}"/>
 <circle cx="34.5" cy="37" r="3" fill="{SKIN}"/><circle cx="65.5" cy="37" r="3" fill="{SKIN}"/>
 <path d="M34 33 Q35 16 51 17 Q67 17 66 33 Q61 24 50 25.5 Q40 25 34 33 Z" fill="#5b3a1e"/>
 <circle cx="44" cy="36" r="1.9" fill="{C['ink']}"/><circle cx="56" cy="36" r="1.9" fill="{C['ink']}"/>
 <path d="M40.5 31.5 q3.5 -2 7 0 M52.5 31.5 q3.5 -2 7 0" stroke="#5b3a1e" stroke-width="1.6" fill="none" stroke-linecap="round"/>
 <path d="M43.5 42.5 Q50 48.5 56.5 42.5" stroke="{C['ink']}" stroke-width="1.8" fill="none" stroke-linecap="round"/>
</symbol>'''
CHAR_PROFA = f'''<symbol id="ch-profa" viewBox="0 0 100 170">
 <ellipse cx="50" cy="164" rx="28" ry="5" fill="#000" opacity=".13"/>
 <rect x="40" y="112" width="8" height="46" rx="3" fill="{SKIN}"/><rect x="52" y="112" width="8" height="46" rx="3" fill="{SKIN}"/>
 <ellipse cx="43" cy="159" rx="8" ry="3.6" fill="{C['red']}"/><ellipse cx="57" cy="159" rx="8" ry="3.6" fill="{C['red']}"/>
 <path d="M32 96 H68 L72 124 H28 Z" fill="#2b3445"/>
 <path d="M31 62 Q50 55 69 62 L70 100 H30 Z" fill="{C['blue']}"/>
 <path d="M44 59 L50 76 L56 59 Z" fill="#fff"/>
 <path d="M31 64 Q22 84 26 104 L33 104 Q31 86 37 70 Z" fill="{C['blue']}"/><circle cx="29.5" cy="106" r="5" fill="{SKIN}"/>
 <path d="M68 63 L87 40 L93 45 L74 72 Z" fill="{C['blue']}"/><circle cx="90.5" cy="41" r="5.2" fill="{SKIN}"/>
 <rect x="89" y="27" width="3.4" height="11" rx="1.7" fill="{SKIN}"/>
 <path d="M31 40 Q30 14 50 15 Q71 15 69 40 Q70 56 63 60 L37 60 Q30 56 31 40Z" fill="#3a2414"/>
 <rect x="45.5" y="48" width="9" height="11" rx="3" fill="{SKIN}"/>
 <circle cx="50" cy="35" r="15.5" fill="{SKIN}"/>
 <path d="M34.5 33 Q36 18 51 18.5 Q63 19 66 31 Q57 27 52 21 Q46 29 34.5 33Z" fill="#3a2414"/>
 <circle cx="44" cy="37" r="1.9" fill="{C['ink']}"/><circle cx="56" cy="37" r="1.9" fill="{C['ink']}"/>
 <path d="M43.5 43 Q50 48.5 56.5 43" stroke="{C['ink']}" stroke-width="1.8" fill="none" stroke-linecap="round"/>
 <circle cx="35" cy="42" r="1.8" fill="{C['gold']}"/><circle cx="65" cy="42" r="1.8" fill="{C['gold']}"/>
</symbol>'''

def char(which="prof", w=70):
    return f'<svg viewBox="0 0 100 170" width="{w}"><use href="#ch-{which}"/></svg>'

# ---------------- boxes ----------------
def esc(s): return s  # conteúdo já em HTML

def lei(art, texto, ref=""):
    r = f'<p class="ref">{ref}</p>' if ref else ''
    return f'''<div class="box lei"><svg class="ic" viewBox="0 0 24 24" style="color:{C['golddeep']}"><rect x="2" y="2" width="20" height="20" rx="5" fill="{C['goldsoft']}"/><use href="#i-book" x="3" y="3" width="18" height="18"/></svg>
<div class="tx"><div class="art">{art}</div>{texto}{r}</div></div>'''

_ch_toggle = [0]
def traduz(texto, who=None, tag="Em outras palavras"):
    if who is None:
        who = "prof" if _ch_toggle[0] % 2 == 0 else "profa"; _ch_toggle[0] += 1
    return f'''<div class="box traduz"><div class="ch">{char(who, 58)}</div><div class="tx"><div class="tag">{tag}</div>{texto}</div></div>'''

def memo(texto, k="Memorize:"):
    return f'''<div class="box memo"><svg class="ic" style="color:#2a1d00"><use href="#i-bulb"/></svg><div><p><b class="k">{k}</b> {texto}</p></div></div>'''

def pega(texto, titulo="Pegadinha de concurso"):
    return f'''<div class="box pega"><div class="bar">{icon('alert')}{titulo}</div><div class="bd">{texto}</div></div>'''

def ex(texto, titulo="Exemplo prático"):
    return f'''<div class="ex box"><div class="lbl">{icon('people')}{titulo}</div>{texto}</div>'''

def oque(texto, titulo="O que é?"):
    return f'''<div class="box oque"><div class="lbl">{icon('q')}{titulo}</div>{texto}</div>'''

def prio(texto):
    return f'''<div class="box prio"><div class="lbl">{icon('target')}Prioridade de estudo</div>{texto}</div>'''

def lembre(texto, titulo="Lembre-se"):
    return f'''<div class="box lembre"><div class="lbl">{icon('pin')}{titulo}</div>{texto}</div>'''

def kw(words):
    chips = "".join(f'<span class="chip">{w}</span>' for w in words)
    return f'''<div class="box kw"><div class="lbl">{icon('key')}Palavras-chave</div><div class="chips">{chips}</div></div>'''

def table(head, rows, widths=None, rh=True):
    th = "".join(f'<th{f" style=\"width:{widths[i]}\"" if widths and widths[i] else ""}>{h}</th>' for i, h in enumerate(head))
    trs = ""
    for r in rows:
        tds = "".join((f'<td class="rh">{c}</td>' if (i == 0 and rh) else f'<td>{c}</td>') for i, c in enumerate(r))
        trs += f"<tr>{tds}</tr>"
    return f"<table><tr>{th}</tr>{trs}</table>"

def cards(items, cols=3):
    out = []
    for it in items:
        ic, title, text = it[0], it[1], it[2]
        top = (f'<div class="letter">{ic[1:]}</div>' if ic.startswith("#") else
               f'<svg class="ci" style="color:{it[3] if len(it)>3 else C["blue"]}"><use href="#i-{ic}"/></svg>')
        out.append(f'<div class="card">{top}<h4>{title}</h4><p>{text}</p></div>')
    return f'<div class="cards c{cols}">{"".join(out)}</div>'

# ---------------- fluxo de ícones "Entenda na prática" ----------------
PAL = [(C['blue'], C['sky']), (C['golddeep'], C['goldsoft']), (C['red'], C['redsoft']), (C['green'], C['greensoft']), (C['navy'], '#e3e9f3')]

def flow(steps, caption="", arrow="→", width=640, colors=None):
    """steps: lista de (icone, [linhas do rótulo]). Desenha tiles com ícone + rótulo e setas."""
    n = len(steps)
    gap = 34
    tile = min(118, (width - gap * (n - 1) - 10) / n)
    total = n * tile + (n - 1) * gap
    x0 = (width - total) / 2
    maxl = max(len(s[1]) for s in steps)
    h = 22 + tile * 0.56 + 18 + maxl * 17 + 6
    parts = [f'<svg viewBox="0 0 {width} {h:.0f}" width="{width-20}" xmlns="http://www.w3.org/2000/svg" font-family="Inter">',
             '<defs><marker id="fa" markerWidth="10" markerHeight="10" refX="8" refY="5" orient="auto"><path d="M0,0 L10,5 L0,10 z" fill="#16202f"/></marker></defs>']
    for i, (ic, lines) in enumerate(steps):
        fg, bg = (colors[i] if colors else PAL[i % len(PAL)])
        x = x0 + i * (tile + gap)
        cx = x + tile / 2
        s = tile * 0.56
        parts.append(f'<rect x="{cx - s/2:.1f}" y="10" width="{s:.1f}" height="{s:.1f}" rx="{s*0.22:.1f}" fill="{bg}" stroke="{fg}" stroke-width="2.5"/>')
        ins = s * 0.62
        parts.append(f'<g style="color:{fg}"><use href="#i-{ic}" x="{cx - ins/2:.1f}" y="{10 + (s-ins)/2:.1f}" width="{ins:.1f}" height="{ins:.1f}"/></g>')
        for j, ln in enumerate(lines):
            wgt = "900" if j == 0 else "500"
            fz = 13.5 if j == 0 else 11.5
            col = C['ink'] if j == 0 else C['muted']
            parts.append(f'<text x="{cx:.1f}" y="{10 + s + 22 + j*17:.1f}" text-anchor="middle" font-size="{fz}" font-weight="{wgt}" fill="{col}">{ln}</text>')
        if i < n - 1:
            ay = 10 + s / 2
            parts.append(f'<line x1="{x + tile/2 + s/2 + 6:.1f}" y1="{ay:.1f}" x2="{x + tile + gap + tile/2 - s/2 - 8:.1f}" y2="{ay:.1f}" stroke="#16202f" stroke-width="3" marker-end="url(#fa)"/>')
    parts.append('</svg>')
    cap = f'<figcaption>{caption}</figcaption>' if caption else ''
    return f'<div class="flow">{"".join(parts)}{cap}</div>'

def pratica_title(t="Entenda na prática"):
    return f'<div class="pratica-title">{t}</div>'

def head(unit, unit_t, title, lead, marker=None):
    m = f'<div class="marker">§§{marker}§§</div>' if marker else ''
    return f'''{m}<div class="unit"><span class="u">{unit}</span><span class="t">{unit_t}</span></div><h1 class="big">{title}</h1><p class="lead">{lead}</p>'''

def page(content, first=False):
    return f'<section class="pg{" first" if first else ""}">{content}</section>'
