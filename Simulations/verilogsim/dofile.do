add wave -position insertpoint  \
sim/:tb_plot_format:A \
sim/:tb_plot_format:initdone \
sim/:tb_plot_format:clock \
sim/:tb_plot_format:Z \

run -all
