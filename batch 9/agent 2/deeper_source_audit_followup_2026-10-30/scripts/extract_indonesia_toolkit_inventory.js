#!/usr/bin/env node
/* Extract the exact Indonesia asset inventory from a pinned user-toolkit snapshot. */
'use strict';

const fs = require('fs');
const path = require('path');

const sourceRoot = process.argv[2];
const commit = process.argv[3] || '';
if (!sourceRoot) {
  console.error('Usage: node extract_indonesia_toolkit_inventory.js SNAPSHOT_ROOT [COMMIT]');
  process.exit(2);
}

const region = 'mapbiomas-indonesia';
const lulc = require(path.join(sourceRoot, 'data', 'collections-lulc.js')).collections[region];
const fire = require(path.join(sourceRoot, 'data', 'collections-fire.js')).collections[region];
const territories = require(path.join(sourceRoot, 'data', 'territories.js')).tables[region];
const rows = [];

function addCollections(product, collections) {
  Object.entries(collections).forEach(([collection, definition]) => {
    Object.entries(definition.assets).forEach(([assetRole, assetId]) => {
      let periodKey = assetRole;
      if (product === 'LULC') {
        periodKey = {integration: 'Coverage', transitions: 'Transitions', quality: 'Quality'}[assetRole];
      }
      const periods = definition.periods[periodKey] || [];
      rows.push({
        asset_class: 'product',
        product,
        collection,
        asset_role: assetRole,
        label: '',
        asset_id: assetId,
        period_key: periodKey,
        period_count: periods.length,
        periods
      });
    });
  });
}

addCollections('LULC', lulc);
addCollections('Fire', fire);
territories.forEach((entry) => {
  rows.push({
    asset_class: 'territory',
    product: 'Territory',
    collection: '',
    asset_role: 'region_of_interest',
    label: entry.label,
    asset_id: entry.value,
    period_key: '',
    period_count: 0,
    periods: []
  });
});

const productRows = rows.filter((row) => row.asset_class === 'product');
const territoryRows = rows.filter((row) => row.asset_class === 'territory');
const result = {
  repository: 'mapbiomas/user-toolkit',
  commit,
  region,
  generated_from: [
    'data/collections-lulc.js',
    'data/collections-fire.js',
    'data/territories.js'
  ],
  summary: {
    product_assets: productRows.length,
    lulc_assets: productRows.filter((row) => row.product === 'LULC').length,
    fire_assets: productRows.filter((row) => row.product === 'Fire').length,
    territory_assets: territoryRows.length,
    lulc_collections: Object.keys(lulc),
    fire_collections: Object.keys(fire),
    reference_or_tvi_assets: 0
  },
  assets: rows
};

if (result.summary.product_assets !== 16 || result.summary.lulc_assets !== 10 ||
    result.summary.fire_assets !== 6 || result.summary.territory_assets !== 24) {
  throw new Error('Unexpected Indonesia inventory counts; inspect upstream definitions before publishing.');
}

const destination = process.argv[4];
const text = JSON.stringify(result, null, 2) + '\n';
if (destination) {
  fs.writeFileSync(destination, text);
} else {
  process.stdout.write(text);
}
