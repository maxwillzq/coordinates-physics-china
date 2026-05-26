import React from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import Layout from '@theme/Layout';
import Heading from '@theme/Heading';
import styles from '@site/src/pages/index.module.css';

function HomepageHeader() {
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          Coordinates: China in the World Map of Physics
        </Heading>
        <p className="hero__subtitle">Explore the historical coordinates and paradigm shifts of China in the world map of physics.</p>
        <div className={styles.buttons}>
          <Link
            className="button button--secondary button--lg"
            to="/en/docs/part1">
            Start Reading
          </Link>
        </div>
      </div>
    </header>
  );
}

export default function Home() {
  return (
    <Layout
      title="Coordinates: China in the World Map of Physics"
      description="Explore the historical coordinates and paradigm shifts of China in the world map of physics.">
      <HomepageHeader />
      <main>
        <div className="container text--center padding-vert--xl">
          <p style={{fontSize: '1.2rem', color: '#666'}}>
            Exploring the historical coordinates and paradigm shifts of China in the world map of physics.
          </p>
        </div>
      </main>
    </Layout>
  );
}
