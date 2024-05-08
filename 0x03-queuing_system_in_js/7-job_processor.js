import { createQueue } from 'kue';

const BLACKLIST = ['4153518780', '4153518780'];
const TOTAL = 100;
const queue = createQueue();

function sendNotification(phoneNumber, message, job, done) {
  function next(p) {
    if (p === 0 || p === (TOTAL / 2)) {
      job.progress(p, TOTAL);

      if (p === (TOTAL / 2)) {
        console.log(`Sending notification to ${phoneNumber}, with message: ${message}`);
      }
    }
    if (BLACKLIST.includes(phoneNumber)) {
      done(new Error(`Phone number ${phoneNumber} is blacklisted`));
    }
    if (p === TOTAL) {
      return done();
    }
    return next(p + 1);
  }
  next(0);
}

queue.process('push_notification_code_2', (job, done) => {
  sendNotification(job.data.phoneNumber, job.data.message, job, done);
  done();
});
