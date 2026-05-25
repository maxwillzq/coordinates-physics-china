import React, { useEffect, useRef } from 'react';
import { useColorMode } from '@docusaurus/theme-common';

export default function Comment() {
  const { colorMode } = useColorMode();
  const commentRef = useRef(null);

  useEffect(() => {
    const script = document.createElement('script');
    script.src = 'https://giscus.app/client.js';
    script.setAttribute('data-repo', 'maxwillzq/coordinates-physics-china');
    script.setAttribute('data-repo-id', 'R_kgDOSne5Qg');
    script.setAttribute('data-category', 'General');
    script.setAttribute('data-category-id', 'DIC_kwDOSne5Qs4C91uy');
    script.setAttribute('data-mapping', 'pathname');
    script.setAttribute('data-strict', '0');
    script.setAttribute('data-reactions-enabled', '1');
    script.setAttribute('data-emit-metadata', '0');
    script.setAttribute('data-input-position', 'bottom');
    script.setAttribute('data-theme', colorMode === 'dark' ? 'dark' : 'light');
    script.setAttribute('data-lang', 'zh-CN');
    script.setAttribute('crossorigin', 'anonymous');
    script.async = true;

    const currentRef = commentRef.current;
    if (currentRef) {
      currentRef.appendChild(script);
    }

    return () => {
      if (currentRef) {
        currentRef.innerHTML = '';
      }
    };
  }, [colorMode]);

  return <div ref={commentRef} className="giscus-container" style={{ marginTop: '2rem' }} />;
}
