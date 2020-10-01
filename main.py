import funcs

def main():
  #funcs.search_company_stock_history()
  close_px, mavg, input = funcs.compute_rolling_average()
  funcs.plot_rolling_average(close_px, mavg, input)

if __name__ == "__main__":
  main()

