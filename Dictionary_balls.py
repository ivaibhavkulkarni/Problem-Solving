def ball_color_score_dic(ball_color_score):
    ball_color_score_dictionary = {}
    for ball_deatils in ball_color_score:
        ball_deatils_list = ball_deatils.split(":")
        print(ball_deatils_list)
        ball_color ,ball_score = ball_deatils_list[0] , int(ball_deatils_list[1])
        if ball_color in ball_color_score_dictionary:
            score = ball_color_score_dictionary[ball_color]
            total_score = ball_score + score
            ball_color_score_dictionary[ball_color] = total_score
            
        else:
            ball_color_score_dictionary[ball_color] = ball_score
    
    return ball_color_score_dictionary 


ball_color_score = input().split(",")
final = ball_color_score_dic(ball_color_score)
print(final)