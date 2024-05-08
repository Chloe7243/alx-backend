function createPushNotificationsJobs(jobs, queue) {
  if (!(jobs instanceof Array)) {
    throw new Error('Jobs is not an array');
  }
  jobs.forEach((job) => {
    job = queue.create('push_notification_code_2', job)
    job
      .on('complete', () => {
        console.log(`Notification job ${job.id} completed`)
      })
      .on('failed', (err) => {
        console.log(`Notification job ${job.id} failed: ${err.message || err.toString()}`)
      })
      .on('progress', (progress, data) => {
        console.log(`Notification job ${job.id} ${progress}% complete`)
      })
      .save((err) => {
        if (!err) console.log("Notification job created:", job.id);
      });
  });
}

module.exports = createPushNotificationsJobs;
