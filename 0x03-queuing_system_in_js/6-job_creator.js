import { createQueue } from 'kue';

const queue = createQueue();

const data = {
  phoneNumber: '+2348145840729',
  message: 'Purchase Airtime',
}

const job = queue
  .create('push_notification_code', data)
  .on('complete', () => {
    console.log("Notification job completed")
  })
  .on('failed', () => {
    console.log("Notification job failed")
  })
  .save((err) => {
    if (!err) console.log("Notification job created:", job.id);
  });
