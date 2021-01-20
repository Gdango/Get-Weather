from apscheduler.schedulers.blocking import BlockingScheduler
import api_request
import app

sched = BlockingScheduler()

@sched.scheduled_job('cron', month='*', day='*', hour=9, minute=30)
def scheduled_job():
    app.main()

sched.start()
