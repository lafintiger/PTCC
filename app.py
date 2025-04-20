with gr.Group():
    with gr.Group():
        with gr.Group():
            resource_alerts = gr.Markdown("No alerts", label="Resource Alerts")

    with gr.Column(scale=3):
        with gr.Group():
            active_tasks_count = gr.Markdown("No active tasks", label="Active Tasks") 