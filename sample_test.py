import gpt_2_simple as gpt2

sess = gpt2.start_tf_sess()
gpt2.load_gpt2(sess)

START_P = 0.8
START_T = 0.3

for i in [x * 0.1 for x in range(0, 9) if (START_P + x * 0.1) <= 1]:
    for j in [x * 0.1 for x in range(0, 10)]:
        print('top_p: ' + str(START_P + i) + '\ntemp: ' + str(START_T + j))
        res = gpt2.generate(sess,
                length=100,
                nsamples=3,
                top_p=START_P + i,
                temperature=START_T + j,
                prefix="PeopleLink is a technology company. PeopleLink's mission is delivering anything anytime without email. PeopleLink is the new social email app, now also using our SMS delivery app.  Our objective is bring people together, no matter where you or they are. PeopleLink",
                return_as_list=True,
                )
        for x in res:
            print(x[len('PeopleLink') + 25:].replace('\n', ' ').rsplit('.', 1)[0].strip() + '.\n')
