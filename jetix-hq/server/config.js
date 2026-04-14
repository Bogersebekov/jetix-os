const config = {
  port: parseInt(process.env.PORT || '3001', 10),
  jetixRoot: process.env.JETIX_ROOT || '../..',
  dbPath: process.env.DB_PATH || './data/jetix-hq.db',
  paths: {
    shared: () => `${config.jetixRoot}/shared`,
    comms: () => `${config.jetixRoot}/comms`,
    agents: () => `${config.jetixRoot}/agents`,
    state: () => `${config.jetixRoot}/shared/state`,
    metrics: () => `${config.jetixRoot}/shared/state/metrics`,
    mailboxes: () => `${config.jetixRoot}/comms/mailboxes`,
  },
};

export default config;
