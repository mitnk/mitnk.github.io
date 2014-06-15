...

The process can be a bit frustrating at times, as there are a lot of
open tickets and not too much committer time available. In addition,
just now 1.4 polishing is the first priority. But you can always help
the project by reviewing/triaging some tickets! If you do that, I
think there is actually a 5-for-1 trade available: triage 5 tickets,
get your ticket reviewed by a core developer.

The triaging process is actually pretty simple: take an unreviewed
ticket. If it is valid (the feature proposal makes sense/there is a
clear bug you can repeat) mark it as accepted. If there is not enough
information mark it as needsinfo. Otherwise invalid or worksforme. (I
don't think it is that important which one you pick). If unsure, just
leave a comment explaining your findings.

Reviewing: take a ticket which is accepted and has a patch. If the
patch is in your opinion ready, mark it as ready for checkin. If not,
leave a comment explaining what is wrong and check the "patch needs
improvement" box. Check the docs for when a patch should be considered
ready for checkin. If unsure, just leave a comment.

Remember that the process aims for high quality patches. When a
committer takes a ticket from "ready from checkin" queue, there should
be some confidence that the ticket is actually high quality and ready
for checkin. That is important, not the exact rules of the process.

Note: this is just my view of the process, nothing official...

From [django-dev maillist](https://groups.google.com/forum/?fromgroups#!topic/django-developers/-QIm4YCkQKI) by Anssi Kääriäinen