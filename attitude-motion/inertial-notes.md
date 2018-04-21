## Altitude sensor
Should I use z acceleration only? Is that gained using derivatives that would then accumulate a lot of error?

I could take the absolute position and correct my values. If I get my z to not match somehow, I might be able to correct my change vectors. Who knows?
* If I would update the change vectors, then that would involve breaking them out into a separate thing and then adding initial conditions somehow. I'm worried that could be really complicated.
* Would that mean that I should just solve these together somehow? I'm already thinking about that and this could be another reason.
  - It seems like you can't break initial conditions out of the vectors. I could for v, but r depends on the conditions for v in an inner integral, at least as it is right now.