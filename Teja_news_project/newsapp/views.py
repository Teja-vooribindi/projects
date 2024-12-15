from django.shortcuts import render
def home_view(request):
    return render(request,'newsapp/home.html')

def movie_news(request):
    news1='Upcoming Film Releases: Several highly anticipated films are set to release soon, with stars like Mahesh Babu, Pawan Kalyan, and Allu Arjun leading the way. Fans are eagerly awaiting trailers and promotional events.'

    news2='Box Office Performances: Recent releases have shown impressive box office performances, with movies breaking records and surpassing previous earnings. Analysis of the reasons behind their success is a hot topic among fans and critics.'

    news3='Awards and Recognitions: Tollywood actors and filmmakers have been nominated for various awards at national and international film festivals. Highlights include nominations for Best Actor, Best Film, and recognition for technical achievements.'

    news4='New Projects and Collaborations: Tollywood is buzzing with news of new collaborations between directors and actors. Notable directors are teaming up with popular stars, promising exciting narratives and fresh concepts.'

    news5='OTT Releases and Trends: The trend of Tollywood films being released on OTT platforms has gained momentum. Viewers are discussing the impact of these releases on traditional cinema, with many films premiering simultaneously in theaters and on streaming services.'

    my_dict={'mnews1':news1,'mnews2':news2,'mnews3':news3,'mnews4':news4,'mnews5':news5,}


    return render(request,'newsapp/movies.html',my_dict)


def political_news(request):
        news1='Legislative Assembly Session: Governor S. Abdul Nazeer has summoned the Legislative Assembly and Council to meet on November 11 for their respective sessions in Amaravati​'

        news2='Water Release for Agriculture: Water has been released to Ravulacheruvu village in the Dharmavaram constituency, aimed at supporting local agriculture​'

        news3='Political Criticism: Pawan Kalyan, the Deputy Chief Minister, has criticized land grabs in the state and called for stricter police action against anti-social elements​'

        news4='Weather Forecast: The weather department has predicted light to moderate rainfall across Andhra Pradesh for the next three days, which may affect local conditions​'

        news5='Suicide of Government Staffer: A tragic incident occurred as a government employee in Karnataka committed suicide due to feelings of injustice, highlighting the need for better support systems for public servants​.'

        my_dict={'pnews1':news1,'pnews2':news2,'pnews3':news3,'pnews4':news4,'pnews5':news5,}


        return render(request,'newsapp/politics.html',my_dict)

def sports_news(request):
        news1="ICC Women's ODI Rankings: Harmanpreet Kaur has made a significant comeback, moving up nine spots to re-enter the top 10 following her impactful performance in the ODI series against New Zealand, where she played a match-winning half-century​​"

        news2="Football Friendly Announcement: India's football coach Manolo Marquez has named a 26-member probable list for an upcoming friendly match against Malaysia, scheduled for November 18 in Hyderabad. This match is part of India's preparation for future international competitions​​"

        news3="Hockey India League: The men's Hockey India League is set to resume on December 28, while the women's league will start on January 12, 2025. Both leagues promise exciting matches with several teams from across the country​"

        news4="Wrestling News: At the recent World Wrestling Championships, Indian wrestler Mansi Ahlawat clinched a bronze medal, while Sandeep Mann unfortunately exited the competition without a medal in mens freestyle wrestling​"

        news5="Olympics Bid: The Indian Olympic Association has officially expressed its interest in hosting the Olympic and Paralympic Games in 2036, submitting a formal Letter of Intent to the International Olympic Committee​."

        my_dict={'snews1':news1,'snews2':news2,'snews3':news3,'snews4':news4,'snews5':news5,}


        return render(request,'newsapp/sports.html',my_dict)