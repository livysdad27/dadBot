# dadBot
Experimental slack bot

#Regression Test/Sign-Off Notes

###This is what is being done by the Product Owner to sign-off on stories.  This list is dynamic and will change periodically.

1. Patient - Sign into [https://th.dev.provinnovate.com/dogfood](https://th.dev.provinnovate.com/dogfood) as TeleHeathPresenterTZ in one window using the dogfood endpoint.  Note that anyone with the presenter role in AD will work.
    a. Create a conference
2. Patient - waiting room
    a. Click on the conference to start it.
    b. The camera should light up.
    c. Double-check waiting room layout
    d. Ask a question
    e. Test My Connection - click retest, then proceed
3. Provider - joins conference
    a. Open the conference from an incognito browser window, and sign in using your p number.
    b. In the conference URL, replace "conference" with "visit" to ensure that endpoint works.  It should look something like: [https://th.dev.provinnovate.com/visit/bNjiWOjc](https://th.dev.provinnovate.com/visit/bNjiWOjc)
    c. Conference should switch to audio\video view
    d. This should be a first run from the browser/incognito window - WebRTC asks for use of the camera and mic *
5. Patient and provider 
    a. Double check layout of video windows look ok
    b. Enable\disable fullscreen
    c. Enable\disable video feed - changes should be reflected on both sides.
    d. Mute\unmute
6. Open/Check the Chat Window
    a. Make sure it flies out.
    b. Enter some text and ensure that populates.
    c. Enter text that is bigger than the window.
    d. Enter so many messages that messages scroll up.
    e. After scrolling up to review them, enter a new message to ensure the focus moves down to the bottom of the chat window.
    f. close the chat window
    g. Reopen it to make sure chat stuff is still there.
    h. Check that when typing, a notification appears on the other side.
7. Disconnect one side from video (one browser window)
8. Reconnect the conference - all is well?

###Other Checks
* Rerun the checks above while disconnecting one side (close of browser and unplug/disable networking) on both sides in different parts of the process.
* Rerun the checks above and disconnect network from either side, reconnect to ensure that the reconnect happens.
* Login as two Telepresenters, see what happens
* Login as two Providers, see what happens.
* Logout on Telepresenter side first and then Provider side first.
* Ensure that feedback is visible in splunk somewhere.
