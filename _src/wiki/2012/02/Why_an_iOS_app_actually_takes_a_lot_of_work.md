from: [kentnguyen.com](http://kentnguyen.com/ios/what-does-it-take-to-make-an-ios-app/)

The big question: How much does an iPhone app cost?

This is a very common question that I’m asked by a lot of my business-oriented friends and non-tech savvy clients. Without fail, every single time I gave my initial estimation before even locking down the specs, I received that shocked expression because of the unexpected (high) quotation.

Yet, none of my quotations has even came close to the range being discussed in this StackOverflow thread, in which the development cost of Twitterific app is discussed. Despite the fact that the original question was asked in 2008 and the best answer (by one of the Twitterific developers) was in 2010, it is still accurate today in Jan 2012 and I can foresee that it will still be true atleast until the end of 2012.

So, with the hype of businesses wanting to have an iOS app continues into 2012, I thought it would make a good post trying to explain why the cost is high by breaking down the steps and variables involved. I hope it will benefit both the non-iOS developers and business people who need to make decisions or just want to understand the process. The ideas in this post are not restricted to just iOS, they are also applicable to other mobile platforms (Android, Windows Mobile, maybe Blackberry) to a large extent.
Checklist: Getting ready for the iPhone app

The process is not a simple one and I usually guide/educate the client through all the considerations using the following steps:

FIRST: One of the most shocking discovery I have after speaking to several clients is that they have no idea about the big infrastructure picture needed for an iPhone application. Because of that they always assume iPhone app is only an app, they expect me to quote them the price for making everything possible within an app without regard to issues such as: do they have a supporting server that the iPhone speaks to, where do they store users’ data (I’m using layman terms here). The first time I met such a client I was furious, however, later on I came to a realization that because the client-server network concept has boiled in my blood since I started programming, I took it for granted that everyone knows. But I was wrong, business-type person doesn’t care and they might not have the technical common-sense you expect.

So to non-tech savvy readers: You need to have a server to store your data if you are looking to do an app that has some kind of authentication/login, or some kind of customization that you want to change it yourself at any time, or even involving simplest form of receiving information from the user (again, i’m using very simple language here).

SECOND: Because of the fact that you need a server, you need to have a way for the iPhone to communicate with the server, sending data to and receiving data from this server. There is no standard way, there is no plug-and-play way to do it, everything has to be customized. This is analogous to creating your own set of language: you don’t want others to understand what you are speaking with your server but two ends need to understand one another.

This is called creating a set of API endpoints (or simply APIs) for your application. These APIs must be in existence before you can proceed to make the iPhone app. Why? Because you need to define the language, before you can communicate! That brings me to the next step, how to create these APIs.

THIRD: Do not take this step lightly, APIs should be viewed as important as 50% of the entire solution. Making APIs is almost like making a full website. You need to first define your data models, the business rules, what are the input parameters of your business logics, how do the data models interact with each other when an event happens. To put it very simply, the outcome is a fully functional website but the pages do not show graphical results, they show only text: an example successful authentication page only contains a single word YES.

The iPhone then makes requests to these pre-determined endpoints (login page) with the pre-determined format of inputs (user+password) then interprets the result that these pages return (YES/NO). The app doesn’t magically register and login the user by itself.

There are *a lot* of variables to be considered in this phrase such as how to pick the server, how to select the language that will be written in, where to host your data to minimise communication delays, etc. I won’t get into details because if you don’t know, you should ask your tech-cofounder or let the developer decide.

FOURTH: Either you need to have this set of APIs ready, well documented by your in-house team to give to your iPhone developer or prepare to pay more than just for the iPhone app. Depends on the developer that you engage, he might or might not have the skills needed to do what you need. If he does, I suggest you to let him do both because then he knows exactly what APIs to call and what is needed to be done to make the app works.

In the case that you already have APIs, you should expect to let the iPhone developer speak freely with your back-end team beside giving him the documentations; because most of the time, he will need to request more work (more APIs) to be done to support the mobile application.
Now, the iPhone part

Phew, that’s a lot just to get ready for your iOS app but now you can start thinking about the iPhone app itself. In general, everything about iOS is very restrictive. You almost have to define 100% of the scope and lock in the design before the developer can start to code, unlike making websites, developing an iOS app under contract has extremely little leeway for changes:

Design the interface: Whether you will use all standard interface components or customized components that will have to be decided right from the start. Because the architecture of the entire application itself depends on how you want your interface be, how the users should use the app. An example is the standard Tab Bar at the bottom, if you want colors icons instead of the blueish tint, the change in code is substantial!

Tightly integrated code: With websites, you can simply add one more page, then create a link to that page when you needed. However, you can’t do that with iOS app, everything has to be set in the beginning, any changes might result in significant other changes that you might not be able to understand why. The way iOS codes are structured is like a breadboard, everything is hard-wired, you still can change a few things here and there, but if you change the wrong wire, the whole board might stop working. Even extremely well structured code does not increase the flexibility by a lot. Adding an additional email button to ‘About’ screen might only be worth a few more lines of code, but adding a Facebook Like button on the same page is a different story, don’t expect that to be done in a few hours.

Converting an iPhone app to iPhone/iPad universal app: This is the worst ‘additional feature’ found in iPhone development contracts. Because an iPad app is not a frikin’ additional feature. The iPad app is always more complex than iPhone app, and most of the time requires entirely different interface and interaction mechanism. It’s like making an electric bicycle and then convert it to a fuel-powered motorcyle! They are very similar at what they do, but under the hood, the difference is immense.

Take the popular Facebook app (in 2012) as an example, the iPad and iPhone app look similar yet they are very different, the way in which a user interacts with stories is substantially different.
Not only that – the API requirements could also be different underneath: The Denso app, an app that I worked on (which is why I know), has some features exclusive only to the iPad that require additional data from server. Additionally, the iPhone and iPad have very distinct user experiences.
So are you ready to begin?

I hope after reading this, you can get a sense of what is needed for you or your company to develop a mobile app. Unless you are making an offline app (like a Calculator app!) that does not collect any data from users, you are not going to get the app made on the cheap side. After considering all the variables above, if you can’t justify contracting development, then the only other option is hiring full time developers to work in-house for the entire length of the project.

On the other hand, if you decide to go ahead and outsource, then I have one more thing to say: The red tape. If you work in a large corporation or regulated environment, your job is essential in helping the developer avoid the red tape along the way, maybe bend the rules a little. I have spoken to a few large clients and they were very skeptical when I asked to look at their APIs. Either they were not willing to open up as it would violate their policies, can’t blame them; or they have yet a properly defined policy for external data access; or even as bad as the brand guideline requires the app to have company logo on every single screen(!!!). In the end I didn’t work with those clients because I cannot imagine how long it would drag and how much trouble I will get into when I need to ask for additional API support.

P.S You need time, lots of it, so be patient.