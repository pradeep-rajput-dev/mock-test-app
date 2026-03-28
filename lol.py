def send_worker(user_id, target_user_id, course_id, course_info):

    if not login():
        bot.send_message(chat_id=user_id, text="❌ Login failed!")
        return

    try:
        url = LESSONS_URL.format(course_id=course_id)
        r = requests.get(url, headers=headers)
        data = r.json()

        today_classes = data.get("todayclasses", [])

        for cls in today_classes:

            if not running_tasks.get(user_id):
                bot.send_message(chat_id=user_id, text="🛑 Stopped!")
                return

            telegram_send(target_user_id, format_class_message(cls, course_info["name"]))

    except Exception as e:
        print(e)

    bot.send_message(chat_id=user_id, text="✅ Done!")
