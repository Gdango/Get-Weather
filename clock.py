from apscheduler.schedulers.background import BackgroundScheduler

sched = BackgroundScheduler()

@sched.scheduled_job('interval', minutes=1440)
def timed_job():
    print("This task is scheduled")

@sched.scheduled_job('cron', day_of_week='')