import sense_hat, random, time

" lab 2 step 1, switches between initials N and D."

sense = sense_hat.SenseHat()

B = (0, 0, 255)
R = (255, 0, 0)
X = (0, 0, 0)

"Images"

letter_N = [
  X, X, X, X, X, X, X, X,
  X, X, X, X, X, X, X, X,
  X, X, X, X, X, X, X, X,
  X, X, X, X, X, X, X, X,
  X, X, X, X, X, X, X, X,
  X, X, X, X, X, X, X, X,
  X, X, X, X, X, X, X, X,
  X, X, X, X, X, X, X, X
  ]
letter_D = [
  X, X, X, X, X, X, X, X,
  X, X, R, R, X, X, X, X,
  X, X, R, X, R, X, X, X,
  X, X, R, X, X, R, X, X,
  X, X, R, X, X, R, X, X,
  X, X, R, X, R, X, X, X,
  X, X, R, R, X, X, X, X,
  X, X, X, X, X, X, X, X
  ]

sense.clear()

sense.set_pixels(letter_N)
state = "N"

while True:
  events = sense.stick.get_events()
  if events:
    for events in events:
      if events.action == 'up':
        if state == "N":
          state = "D"
          sense.set_pixels(letter_D)
        else:
          continue
      elif events.action == 'down':
          if state == "D":
              state = "N"
              sense.set_pixels(letter_N)
          else:
             continue
                  
        
      