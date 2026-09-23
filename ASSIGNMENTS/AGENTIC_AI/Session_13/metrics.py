def completion_rate(completed, partial, assigned, partial_credit=0.5):
    if assigned<=0: raise ValueError("assigned must be > 0")
    return 100*(completed+partial*partial_credit)/assigned
if __name__=="__main__":
    print(f"Strict completion rate: {100*15/20:.1f}%")
    print(f"Weighted rate (partial task = half credit): {completion_rate(15,2,20):.1f}%")
