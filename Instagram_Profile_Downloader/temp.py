import instaloader

ig = instaloader.Instaloader()
ig.interactive_login(input("Username:"))
profile = input()
# ig.download_tagged(profile)
ig.download_profile(profile, profile_pic=False, profile_pic_only=False, fast_update=False, download_stories=False,
                    download_stories_only=False, download_tagged=True, download_tagged_only=False, post_filter=None,
                    storyitem_filter=None)
