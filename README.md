
# **Welcome!**

Better late than never, I'm doing my introduction to [Streamlit](https://streamlit.io/) to get a better view of my Data Science projects!

The objective of this repository is to help me and you get the idea of what streamlit can do, and how can we do it. Of course there are several projects way ahead of us, and you are free to search for them, but that doesn't mean we can't start now.

I'll always show my references, without them would be a lot harder to progress, and that's the least that I could do for them.

---

## But what is this?

Okay, now what is streamlit? I'm still getting in it, but it would be a python framework that is really clear and simple. Doesn't need to think about front-end  or back-end. The idea is to help projects related to Machine Learning and Data Science to have a fast interactive app related to them. We want to stay simple, if we start building up too much, optimization will fail, and the interactive app will be not as good as you wanted.

Besides that, it is really nice!

## How can we do it?

We are setting up a virtual enviroment through python, and we will work with python files, executing them, using the streamlit server to make things shine. 

### Setting up enviroment

```bash
python3 -m venv .venv

source .venv/bin/activate

pip install streamlit
```

Before even creating a python file we can see what streamlit can do with the next command line:

```bash
streamlit hello
```

Did you see the possibilities? It really is overwhelming and can help us do an application without thinking too much in front or backend, just do the analysis and plot the graphics or whatever you like.

For the applications I'm using a few packages that requires to be installed, so just do a pip install with the requirements and we are settled to run the apps.

```bash
pip install -r requirements.txt
```

The Password Manager and the Smart Trader apps I saw in Medium article that is referenced in the end of the readme. I'm not really into trading (at least for now), but I thought the idea was nice and has a nice appearance in streamlit.

### After creating the python file, we will execute with...

```bash
streamlit run filename.py
```

---

## Final points

* The streamlit version will be shown inside the interactive app (maybe not my smartest idea);
* The example files for the apps will be in the directory called 'files';
* This is a working in progress repository, probably I'll be adding more cases through the weeks, and maybe when I get satisfied, I'll start moving to my Data Science projects.

---

And all props goes to [Eduardo Mendes](https://www.youtube.com/@Dunossauro), who does a great work with his streams! This [one](https://www.youtube.com/watch?v=Ie5ef_R_k6I&ab_channel=EduardoMendes) in particular.

And here is the Medium [article](https://medium.com/pythoneers/10-mindblowing-automation-scripts-you-need-to-try-using-python-8bd935f88125).
