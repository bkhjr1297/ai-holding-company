'use strict';

const fs = require('fs');
const path = require('path');

const ROOT = '/root';
const INTEGRATIONS_DIR = path.join(ROOT, 'ai-holding-company', 'integrations');

const REPOS = {
  agencyAgents: { path: path.join(ROOT, 'agency-agents'), role: 'agent-personas' },
  ecc: { path: path.join(ROOT, 'ECC'), role: 'coding-workflows' },
  karpathySkills: { path: path.join(ROOT, 'andrej-karpathy-skills'), role: 'behavioral-guidance' },
  openDesign: { path: path.join(ROOT, 'open-design'), role: 'design-system' },
  superpowers: { path: path.join(ROOT, 'Superpowers'), role: 'plugin-system' },
  ruflo: { path: path.join(ROOT, 'ruflo'), role: 'react-runtime' },
  cashClaw: { path: path.join(ROOT, 'cashclaw'), role: 'marketplace' },
  habitica: { path: path.join(ROOT, 'habitica'), role: 'gamification' },
  businessRepos: {
    path: path.join(ROOT, 'ai-holding-company', 'businesses'),
    role: 'business-units',
  },
  tribe: {
    path: path.join(ROOT, 'ai-holding-company', 'tribe'),
    role: 'family-fund',
  },
};

const CLI_TOOLS = {
  agentcash: { cmd: 'agentcash', role: 'x402-payments' },
  apibaseMCP: { cmd: 'apibase-mcp', role: 'api-gateway' },
  pinch: { cmd: 'pinch', role: 'wallet-guardrails' },
  mltl: { cmd: 'mltl', role: 'marketplace-cli' },
};

function resolve(repoKey) {
  const repo = REPOS[repoKey];
  if (!repo) {
    throw new Error(`Unknown repo: ${repoKey}`);
  }
  const exists = fs.existsSync(repo.path);
  const brokenReason = exists ? null : 'directory-not-found';
  return {
    key: repoKey,
    path: repo.path,
    role: repo.role,
    present: exists,
    brokenReason,
  };
}

function resolveAll() {
  const result = {};
  for (const key of Object.keys(REPOS)) {
    result[key] = resolve(key);
  }
  return result;
}

function resolveRepos(...keys) {
  return keys.map((k) => resolve(k));
}

function summarize() {
  const repos = resolveAll();
  const summary = [];
  for (const [key, info] of Object.entries(repos)) {
    summary.push({
      repo: key,
      role: info.role,
      present: info.present,
      brokenReason: info.brokenReason,
    });
  }
  return summary;
}

module.exports = {
  REPOS,
  CLI_TOOLS,
  resolve,
  resolveAll,
  resolveRepos,
  summarize,
};
