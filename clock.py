from apscheduler.schedulers.blocking import BlockingScheduler
import api_request
import app

sched = BlockingScheduler()

@sched.scheduled_job('cron', month='*', day='*', hour=21, minute=35)
def scheduled_job:
    app.main()

sched.start()
