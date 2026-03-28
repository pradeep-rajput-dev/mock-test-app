
def send(update: Update, context: CallbackContext):
    user_id = update.effective_chat.id

    if user_id != CHAT_ID:
        update.message.reply_text("❌ Unauthorized")
        return

    args = context.args

    # ❌ गलत usage block
    if len(args) != 2:
        update.message.reply_text("⚠️ Format use kar:\n/send user_id course_id")
        return

    target_user_id = args[0]
    course_id = args[1]

    # validate user_id
    if not target_user_id.lstrip("-").isdigit():
        update.message.reply_text("❌ Invalid user_id")
        return

    target_user_id = int(target_user_id)

    # validate course
    course_info = COURSES.get(course_id)
    if not course_info:
        update.message.reply_text("❌ Invalid course_id")
        return

    running_tasks[user_id] = True

    update.message.reply_text(f"⏳ Sending course {course_id} to {target_user_id}...")

    threading.Thread(
        target=send_worker,
        args=(user_id, target_user_id, course_id, course_info)
    ).start()
