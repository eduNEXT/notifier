from django.core.management.base import BaseCommand

from notifier.tasks import do_forums_digests as do_forums_digests_task


class Command(BaseCommand):

    help = """Run the forum digest job:
    This command was created as an alternative to the scheduler command.
    Since there no scheduler here, you can use Jenkins, for instances, to run this command as a cron
    """

    def handle(self, *args, **options):
        do_forums_digests_task.delay()
