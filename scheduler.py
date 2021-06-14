import schedule
import time
import couch_calls
import gpio_calls

def check_sensors():
    print("Checking sensors")
    couch_calls.add_record(gpio_calls.query_light(), 'light')
    couch_calls.add_record(gpio_calls.query_water_temp(), 'temp')

def init_db():
    couch_calls.init()    

def init_schedule():
    schedule.every(5).minutes.do(check_sensors) #only for mockups, do not use in real case scenario (the db will explode)
    # schedule.every().hour.do(check_sensors)

def start_loop():
    while True:
        schedule.run_pending()
        time.sleep(1)


if __name__ == "__main__":
    init_db()
    init_schedule()
    start_loop()

