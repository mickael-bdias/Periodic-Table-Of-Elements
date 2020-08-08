import tkinter as root
from tkinter import ttk

from PIL import ImageTk, Image


# Variables for the padding (frames, etc)
pad_x = 1
pad_y = 1
entry_box = 19
pad_box_x = 1
pad_box_y = 1


class Elements(root.Frame):
    def __init__(self, parent, controller):
        root.Frame.__init__(self, parent)
        self.parent = parent

        # Frames
        frame_elements = root.LabelFrame(self, padx=2, pady=2)
        frame_elements.grid(row=0, column=0, columnspan=4)

        frame_basic_data = root.LabelFrame(self, text="Basic information", padx=2, pady=13)
        frame_basic_data.grid(row=1, column=0)

        frame_data = root.LabelFrame(self, text="In the periodic table", padx=2, pady=2)
        frame_data.grid(row=1, column=1)

        frame_physical_properties = root.LabelFrame(self, text="Physical properties", padx=2, pady=2)
        frame_physical_properties.grid(row=1, column=2)

        frame_atomic_properties = root.LabelFrame(self, text="Atomic properties", padx=2, pady=2)
        frame_atomic_properties.grid(row=1, column=3)

        frame_other_properties = root.LabelFrame(self, text="Other properties", padx=3, pady=2)
        frame_other_properties.grid(row=2, column=0)

        frame_history = root.LabelFrame(self, text="History", padx=11, pady=2)
        frame_history.grid(row=2, column=1)

        frame_image = root.LabelFrame(self, text="Discoverer | Element", padx=2, pady=2)
        frame_image.grid(row=2, column=2)

        def hydrogen():
            # frame_basic_data
            atomic_number_hydrogen = ttk.Label(frame_basic_data, text="1", width=entry_box)
            atomic_number_hydrogen.grid(row=0, column=1, padx=pad_box_x, pady=pad_box_y)
            symbol_hydrogen = ttk.Label(frame_basic_data, text="H", width=entry_box)
            symbol_hydrogen.grid(row=1, column=1, padx=pad_box_x, pady=pad_box_y)
            name_hydrogen = ttk.Label(frame_basic_data, text="Hydrogen", width=entry_box)
            name_hydrogen.grid(row=2, column=1, padx=pad_box_x, pady=pad_box_y)
            atomic_number_hydrogen = ttk.Label(frame_basic_data, text="1.0079", width=entry_box)
            atomic_number_hydrogen.grid(row=3, column=1, padx=pad_box_x, pady=pad_box_y)
            # frame_data
            group_hydrogen = ttk.Label(frame_data, text="1:H and alkali metals", width=entry_box)
            group_hydrogen.grid(row=0, column=1, padx=pad_box_x, pady=pad_box_y)
            period_hydrogen = ttk.Label(frame_data, text="Period 1", width=entry_box)
            period_hydrogen.grid(row=1, column=1, padx=pad_box_x, pady=pad_box_y)
            block_hydrogen = ttk.Label(frame_data, text="S-block", width=entry_box)
            block_hydrogen.grid(row=2, column=1, padx=pad_box_x, pady=pad_box_y)
            electron_config_hydrogen = ttk.Label(frame_data, text="1s1", width=entry_box)
            electron_config_hydrogen.grid(row=3, column=1, padx=pad_box_x, pady=pad_box_y)
            electron_shell_hydrogen = ttk.Label(frame_data, text="1", width=entry_box)
            electron_shell_hydrogen.grid(row=4, column=1, padx=pad_box_x, pady=pad_box_y)
            # frame_physical_properties
            stp_hydrogen = ttk.Label(frame_physical_properties, text="Gas", width=entry_box)
            stp_hydrogen.grid(row=0, column=1, padx=pad_box_x, pady=pad_box_y)
            melting_point_hydrogen = ttk.Label(frame_physical_properties, text="13.99", width=entry_box)
            melting_point_hydrogen.grid(row=1, column=1, padx=pad_box_x, pady=pad_box_y)
            boiling_point_hydrogen = ttk.Label(frame_physical_properties, text="20.271", width=entry_box)
            boiling_point_hydrogen.grid(row=2, column=1, padx=pad_box_x, pady=pad_box_y)
            density_hydrogen = ttk.Label(frame_physical_properties, text="0.08988", width=entry_box)
            density_hydrogen.grid(row=3, column=1, padx=pad_box_x, pady=pad_box_y)
            triple_point_hydrogen = ttk.Label(frame_physical_properties, text="13.8033 | 7041", width=entry_box)
            triple_point_hydrogen.grid(row=4, column=1, padx=pad_box_x, pady=pad_box_y)
            critical_point_hydrogen = ttk.Label(frame_physical_properties, text="32.938 | 1285800", width=entry_box)
            critical_point_hydrogen.grid(row=0, column=3, padx=pad_box_x, pady=pad_box_y)
            heat_fusion_hydrogen = ttk.Label(frame_physical_properties, text="0.117", width=entry_box)
            heat_fusion_hydrogen.grid(row=1, column=3, padx=pad_box_x, pady=pad_box_y)
            heat_vapor_hydrogen = ttk.Label(frame_physical_properties, text="0.904", width=entry_box)
            heat_vapor_hydrogen.grid(row=2, column=3, padx=pad_box_x, pady=pad_box_y)
            molar_heat_hydrogen = ttk.Label(frame_physical_properties, text="28.836", width=entry_box)
            molar_heat_hydrogen.grid(row=3, column=3, padx=pad_box_x, pady=pad_box_y)
            vapor_pres_hydrogen = ttk.Label(frame_physical_properties, text="15", width=entry_box)
            vapor_pres_hydrogen.grid(row=4, column=3, padx=pad_box_x, pady=pad_box_y)
            # frame_atomic_properties
            oxidation_hydrogen = ttk.Label(frame_atomic_properties, text="−1, +1", width=entry_box)
            oxidation_hydrogen.grid(row=0, column=1, padx=pad_box_x, pady=pad_box_y)
            electronegative_hydrogen = ttk.Label(frame_atomic_properties, text="2.20", width=entry_box)
            electronegative_hydrogen.grid(row=1, column=1, padx=pad_box_x, pady=pad_box_y)
            ionization_hydrogen = ttk.Label(frame_atomic_properties, text="1312.0", width=entry_box)
            ionization_hydrogen.grid(row=2, column=1, padx=pad_box_x, pady=pad_box_y)
            covalent_radius_hydrogen = ttk.Label(frame_atomic_properties, text="31±5", width=entry_box)
            covalent_radius_hydrogen.grid(row=3, column=1, padx=pad_box_x, pady=pad_box_y)
            waals_hydrogen = ttk.Label(frame_atomic_properties, text="120", width=entry_box)
            waals_hydrogen.grid(row=4, column=1, padx=pad_box_x, pady=pad_box_y)
            # frame_image
            frame_image_dummy.destroy()
            self.hydrogen_01 = ImageTk.PhotoImage(Image.open("Images/001.hydrogen-01.jpg"))
            hydrogen_01_label = ttk.Label(frame_image, image=self.hydrogen_01)
            hydrogen_01_label.grid(row=0, column=0, padx=1, pady=1)
            self.hydrogen_02 = ImageTk.PhotoImage(Image.open("Images/001.hydrogen-02.jpg"))
            hydrogen_02_label = ttk.Label(frame_image, image=self.hydrogen_02)
            hydrogen_02_label.grid(row=0, column=1, padx=1, pady=1)

        def helium():
            # frame_basic_data
            atomic_number_helium = ttk.Label(frame_basic_data, text="2", width=entry_box)
            atomic_number_helium.grid(row=0, column=1, padx=pad_box_x, pady=pad_box_y)
            symbol_helium = ttk.Label(frame_basic_data, text="He", width=entry_box)
            symbol_helium.grid(row=1, column=1, padx=pad_box_x, pady=pad_box_y)
            name_helium = ttk.Label(frame_basic_data, text="Helium", width=entry_box)
            name_helium.grid(row=2, column=1, padx=pad_box_x, pady=pad_box_y)
            atomic_number_helium = ttk.Label(frame_basic_data, text="4.0026", width=entry_box)
            atomic_number_helium.grid(row=3, column=1, padx=pad_box_x, pady=pad_box_y)

        # Creating the H (Hydrogen) element
        button_h = ttk.Button(frame_elements, text="H", command=hydrogen)
        button_h.grid(row=0, column=0, padx=pad_x, pady=pad_y)

        # Creating the He (Helium) element
        button_he = ttk.Button(frame_elements, text="He", command=helium)
        button_he.grid(row=0, column=17, padx=pad_x, pady=pad_y)

        # Creating the Li (Lithium) element
        button_li = ttk.Button(frame_elements, text="Li")
        button_li.grid(row=1, column=0, padx=pad_x, pady=pad_y)

        # Creating the Be (Beryllium) element
        button_be = ttk.Button(frame_elements, text="Be")
        button_be.grid(row=1, column=1, padx=pad_x, pady=pad_y)

        # Creating the B (Boron) element
        button_b = ttk.Button(frame_elements, text="B")
        button_b.grid(row=1, column=12, padx=pad_x, pady=pad_y)

        # Creating the C (Carbon) element
        button_c = ttk.Button(frame_elements, text="C")
        button_c.grid(row=1, column=13, padx=pad_x, pady=pad_y)

        # Creating the N (Nitrogen) element
        button_n = ttk.Button(frame_elements, text="N")
        button_n.grid(row=1, column=14, padx=pad_x, pady=pad_y)

        # Creating the O (Oxygen) element
        button_o = ttk.Button(frame_elements, text="O")
        button_o.grid(row=1, column=15, padx=pad_x, pady=pad_y)

        # Creating the F (Fluorine) element
        button_f = ttk.Button(frame_elements, text="F")
        button_f.grid(row=1, column=16, padx=pad_x, pady=pad_y)

        # Creating the Ne (Neon) element
        button_ne = ttk.Button(frame_elements, text="Ne")
        button_ne.grid(row=1, column=17, padx=pad_x, pady=pad_y)

        # Creating the Na (Sodium) element
        button_na = ttk.Button(frame_elements, text="Na")
        button_na.grid(row=2, column=0, padx=pad_x, pady=pad_y)

        # Creating the Mg (Magnesium) element
        button_mg = ttk.Button(frame_elements, text="Mg")
        button_mg.grid(row=2, column=1, padx=pad_x, pady=pad_y)

        # Creating the Al (Aluminium) element
        button_al = ttk.Button(frame_elements, text="Al")
        button_al.grid(row=2, column=12, padx=pad_x, pady=pad_y)

        # Creating the Si (Silicon) element
        button_si = ttk.Button(frame_elements, text="Al")
        button_si.grid(row=2, column=13, padx=pad_x, pady=pad_y)

        # Creating the P (Phosphorus) element
        button_p = ttk.Button(frame_elements, text="P")
        button_p.grid(row=2, column=14, padx=pad_x, pady=pad_y)

        # Creating the S (Sulfur) element
        button_s = ttk.Button(frame_elements, text="P")
        button_s.grid(row=2, column=15, padx=pad_x, pady=pad_y)

        # Creating the Cl (Chlorine) element
        button_cl = ttk.Button(frame_elements, text="Cl")
        button_cl.grid(row=2, column=16, padx=pad_x, pady=pad_y)

        # Creating the Ar (Argon) element
        button_ar = ttk.Button(frame_elements, text="Ar")
        button_ar.grid(row=2, column=17, padx=pad_x, pady=pad_y)

        # Creating the K (Potassium) element
        button_k = ttk.Button(frame_elements, text="K")
        button_k.grid(row=3, column=0, padx=pad_x, pady=pad_y)

        # Creating the Ca (Calcium) element
        button_ca = ttk.Button(frame_elements, text="Ca")
        button_ca.grid(row=3, column=1, padx=pad_x, pady=pad_y)

        # Creating the Sc (Scandium) element
        button_sc = ttk.Button(frame_elements, text="Sc")
        button_sc.grid(row=3, column=2, padx=pad_x, pady=pad_y)

        # Creating the Ti (Titanium) element
        button_ti = ttk.Button(frame_elements, text="Ti")
        button_ti.grid(row=3, column=3, padx=pad_x, pady=pad_y)

        # Creating the V (Vanadium) element
        button_v = ttk.Button(frame_elements, text="V")
        button_v.grid(row=3, column=4, padx=pad_x, pady=pad_y)

        # Creating the Cr (Chromium) element
        button_cr = ttk.Button(frame_elements, text="Cr")
        button_cr.grid(row=3, column=5, padx=pad_x, pady=pad_y)

        # Creating the Mn (Manganese) element
        button_mn = ttk.Button(frame_elements, text="Mn")
        button_mn.grid(row=3, column=6, padx=pad_x, pady=pad_y)

        # Creating the Fe (Iron) element
        button_fe = ttk.Button(frame_elements, text="Fe")
        button_fe.grid(row=3, column=7, padx=pad_x, pady=pad_y)

        # Creating the Co (Cobalt) element
        button_co = ttk.Button(frame_elements, text="Co")
        button_co.grid(row=3, column=8, padx=pad_x, pady=pad_y)

        # Creating the Ni (Nickel) element
        button_ni = ttk.Button(frame_elements, text="Ni")
        button_ni.grid(row=3, column=9, padx=pad_x, pady=pad_y)

        # Creating the Cu (Copper) element
        button_cu = ttk.Button(frame_elements, text="Cu")
        button_cu.grid(row=3, column=10, padx=pad_x, pady=pad_y)

        # Creating the Zn (Zinc) element
        button_zn = ttk.Button(frame_elements, text="Zn")
        button_zn.grid(row=3, column=11, padx=pad_x, pady=pad_y)

        # Creating the Ga (Gallium) element
        button_ga = ttk.Button(frame_elements, text="Ga")
        button_ga.grid(row=3, column=12, padx=pad_x, pady=pad_y)

        # Creating the Ge (Germanium) element
        button_ge = ttk.Button(frame_elements, text="Ge")
        button_ge.grid(row=3, column=13, padx=pad_x, pady=pad_y)

        # Creating the As (Arsenic) element
        button_as = ttk.Button(frame_elements, text="As")
        button_as.grid(row=3, column=14, padx=pad_x, pady=pad_y)

        # Creating the Se (Selenium) element
        button_se = ttk.Button(frame_elements, text="Se")
        button_se.grid(row=3, column=15, padx=pad_x, pady=pad_y)

        # Creating the Br (Bromine) element
        button_br = ttk.Button(frame_elements, text="Br")
        button_br.grid(row=3, column=16, padx=pad_x, pady=pad_y)

        # Creating the Kr (Krypton) element
        button_kr = ttk.Button(frame_elements, text="Kr")
        button_kr.grid(row=3, column=17, padx=pad_x, pady=pad_y)

        # Creating the Rb (Rubidium) element
        button_rb = ttk.Button(frame_elements, text="Rb")
        button_rb.grid(row=4, column=0, padx=pad_x, pady=pad_y)

        # Creating the Sr (Strontium) element
        button_sr = ttk.Button(frame_elements, text="Sr")
        button_sr.grid(row=4, column=1, padx=pad_x, pady=pad_y)

        # Creating the Y (Yttrium) element
        button_y = ttk.Button(frame_elements, text="Y")
        button_y.grid(row=4, column=2, padx=pad_x, pady=pad_y)

        # Creating the Zr (Zirconium) element
        button_zr = ttk.Button(frame_elements, text="Zr")
        button_zr.grid(row=4, column=3, padx=pad_x, pady=pad_y)

        # Creating the Nb (Niobium) element
        button_nb = ttk.Button(frame_elements, text="Nb")
        button_nb.grid(row=4, column=4, padx=pad_x, pady=pad_y)

        # Creating the Mo (Molybdenum) element
        button_mo = ttk.Button(frame_elements, text="Mo")
        button_mo.grid(row=4, column=5, padx=pad_x, pady=pad_y)

        # Creating the Tc (Technetium) element
        button_tc = ttk.Button(frame_elements, text="Tc")
        button_tc.grid(row=4, column=6, padx=pad_x, pady=pad_y)

        # Creating the Ru (Ruthenium) element
        button_ru = ttk.Button(frame_elements, text="Ru")
        button_ru.grid(row=4, column=7, padx=pad_x, pady=pad_y)

        # Creating the Rh (Rhodium) element
        button_rh = ttk.Button(frame_elements, text="Ru")
        button_rh.grid(row=4, column=8, padx=pad_x, pady=pad_y)

        # Creating the Pd (Palladium) element
        button_pd = ttk.Button(frame_elements, text="Pd")
        button_pd.grid(row=4, column=9, padx=pad_x, pady=pad_y)

        # Creating the Ag (Silver) element
        button_ag = ttk.Button(frame_elements, text="Ag")
        button_ag.grid(row=4, column=10, padx=pad_x, pady=pad_y)

        # Creating the Cd (Cadmium) element
        button_cd = ttk.Button(frame_elements, text="Cd")
        button_cd.grid(row=4, column=11, padx=pad_x, pady=pad_y)

        # Creating the In (Indium) element
        button_in = ttk.Button(frame_elements, text="In")
        button_in.grid(row=4, column=12, padx=pad_x, pady=pad_y)

        # Creating the Sn (Tin) element
        button_sn = ttk.Button(frame_elements, text="Sn")
        button_sn.grid(row=4, column=13, padx=pad_x, pady=pad_y)

        # Creating the Sb (Antimony) element
        button_sb = ttk.Button(frame_elements, text="Sb")
        button_sb.grid(row=4, column=14, padx=pad_x, pady=pad_y)

        # Creating the Te (Tellurium) element
        button_te = ttk.Button(frame_elements, text="Te")
        button_te.grid(row=4, column=15, padx=pad_x, pady=pad_y)

        # Creating the I (Iodine) element
        button_i = ttk.Button(frame_elements, text="I")
        button_i.grid(row=4, column=16, padx=pad_x, pady=pad_y)

        # Creating the Xe (Xenon) element
        button_xe = ttk.Button(frame_elements, text="Xe")
        button_xe.grid(row=4, column=17, padx=pad_x, pady=pad_y)

        # Creating the Cs (Caesium) element
        button_cs = ttk.Button(frame_elements, text="Cs")
        button_cs.grid(row=5, column=0, padx=pad_x, pady=pad_y)

        # Creating the Ba (Barium) element
        button_ba = ttk.Button(frame_elements, text="Ba")
        button_ba.grid(row=5, column=1, padx=pad_x, pady=pad_y)

        # Creating the Lanthanides
        button_lanthanides = ttk.Button(frame_elements, text="Lanthanides", state="disabled")
        button_lanthanides.grid(row=5, column=2, padx=pad_x, pady=pad_y)

        # Creating the Hf (Hafnium) element
        button_hf = ttk.Button(frame_elements, text="Hf")
        button_hf.grid(row=5, column=3, padx=pad_x, pady=pad_y)

        # Creating the Ta (Tantalum) element
        button_ta = ttk.Button(frame_elements, text="Ta")
        button_ta.grid(row=5, column=4, padx=pad_x, pady=pad_y)

        # Creating the W (Tungsten) element
        button_w = ttk.Button(frame_elements, text="W")
        button_w.grid(row=5, column=5, padx=pad_x, pady=pad_y)

        # Creating the Re (Rhenium) element
        button_re = ttk.Button(frame_elements, text="Re")
        button_re.grid(row=5, column=6, padx=pad_x, pady=pad_y)

        # Creating the Os (Osmium) element
        button_os = ttk.Button(frame_elements, text="Os")
        button_os.grid(row=5, column=7, padx=pad_x, pady=pad_y)

        # Creating the Ir (Iridium) element
        button_ir = ttk.Button(frame_elements, text="Ir")
        button_ir.grid(row=5, column=8, padx=pad_x, pady=pad_y)

        # Creating the Pt (Platinum) element
        button_pt = ttk.Button(frame_elements, text="Pt")
        button_pt.grid(row=5, column=9, padx=pad_x, pady=pad_y)

        # Creating the Au (Gold) element
        button_au = ttk.Button(frame_elements, text="Au")
        button_au.grid(row=5, column=10, padx=pad_x, pady=pad_y)

        # Creating the Hg (Mercury) element
        button_hg = ttk.Button(frame_elements, text="Hg")
        button_hg.grid(row=5, column=11, padx=pad_x, pady=pad_y)

        # Creating the Tl (Thallium) element
        button_tl = ttk.Button(frame_elements, text="Tl")
        button_tl.grid(row=5, column=12, padx=pad_x, pady=pad_y)

        # Creating the Pb (Lead) element
        button_pb = ttk.Button(frame_elements, text="Pb")
        button_pb.grid(row=5, column=13, padx=pad_x, pady=pad_y)

        # Creating the Bi (Bismuth) element
        button_bi = ttk.Button(frame_elements, text="Bi")
        button_bi.grid(row=5, column=14, padx=pad_x, pady=pad_y)

        # Creating the Po (Polonium) element
        button_po = ttk.Button(frame_elements, text="Po")
        button_po.grid(row=5, column=15, padx=pad_x, pady=pad_y)

        # Creating the At (Astatine) element
        button_at = ttk.Button(frame_elements, text="At")
        button_at.grid(row=5, column=16, padx=pad_x, pady=pad_y)

        # Creating the Rn (Radon) element
        button_rn = ttk.Button(frame_elements, text="Rn")
        button_rn.grid(row=5, column=17, padx=pad_x, pady=pad_y)

        # Creating the Fr (Francium) element
        button_fr = ttk.Button(frame_elements, text="Fr")
        button_fr.grid(row=6, column=0, padx=pad_x, pady=pad_y)

        # Creating the Ra (Radium) element
        button_ra = ttk.Button(frame_elements, text="Fr")
        button_ra.grid(row=6, column=1, padx=pad_x, pady=pad_y)

        # Creating the Actinides
        button_actinides = ttk.Button(frame_elements, text="Actinides", state="disabled")
        button_actinides.grid(row=6, column=2, padx=pad_x, pady=pad_y)

        # Creating the Rf (Rutherfordium) element
        button_rf = ttk.Button(frame_elements, text="Rf")
        button_rf.grid(row=6, column=3, padx=pad_x, pady=pad_y)

        # Creating the Db (Dubnium) element
        button_db = ttk.Button(frame_elements, text="Db")
        button_db.grid(row=6, column=4, padx=pad_x, pady=pad_y)

        # Creating the Sg (Seaborgium) element
        button_sg = ttk.Button(frame_elements, text="Sg")
        button_sg.grid(row=6, column=5, padx=pad_x, pady=pad_y)

        # Creating the Bh (Bohrium) element
        button_bh = ttk.Button(frame_elements, text="Bh")
        button_bh.grid(row=6, column=6, padx=pad_x, pady=pad_y)

        # Creating the Hs (Hassium) element
        button_hs = ttk.Button(frame_elements, text="Hs")
        button_hs.grid(row=6, column=7, padx=pad_x, pady=pad_y)

        # Creating the Mt (Meitnerium) element
        button_mt = ttk.Button(frame_elements, text="Mt")
        button_mt.grid(row=6, column=8, padx=pad_x, pady=pad_y)

        # Creating the Ds (Darmstadtium) element
        button_ds = ttk.Button(frame_elements, text="Ds")
        button_ds.grid(row=6, column=9, padx=pad_x, pady=pad_y)

        # Creating the Rg (Roentgenium) element
        button_rg = ttk.Button(frame_elements, text="Rg")
        button_rg.grid(row=6, column=10, padx=pad_x, pady=pad_y)

        # Creating the Cn (Copernicium) element
        button_cn = ttk.Button(frame_elements, text="Cn")
        button_cn.grid(row=6, column=11, padx=pad_x, pady=pad_y)

        # Creating the Nh (Nihonium) element
        button_nh = ttk.Button(frame_elements, text="Nh")
        button_nh.grid(row=6, column=12, padx=pad_x, pady=pad_y)

        # Creating the Fl (Flerovium) element
        button_fl = ttk.Button(frame_elements, text="Fl")
        button_fl.grid(row=6, column=13, padx=pad_x, pady=pad_y)

        # Creating the Mc (Moscovium) element
        button_mc = ttk.Button(frame_elements, text="Mc")
        button_mc.grid(row=6, column=14, padx=pad_x, pady=pad_y)

        # Creating the Lv (Livermorium) element
        button_lv = ttk.Button(frame_elements, text="Lv")
        button_lv.grid(row=6, column=15, padx=pad_x, pady=pad_y)

        # Creating the Ts (Tennessine) element
        button_ts = ttk.Button(frame_elements, text="Ts")
        button_ts.grid(row=6, column=16, padx=pad_x, pady=pad_y)

        # Creating the Og (Oganesson) element
        button_og = ttk.Button(frame_elements, text="Og")
        button_og.grid(row=6, column=17, padx=pad_x, pady=pad_y)

        # Creating the La (Lanthanum) element
        button_la = ttk.Button(frame_elements, text="La")
        button_la.grid(row=7, column=2, padx=pad_x, pady=pad_y)

        # Creating the Ce (Cerium) element
        button_ce = ttk.Button(frame_elements, text="Ce")
        button_ce.grid(row=7, column=3, padx=pad_x, pady=pad_y)

        # Creating the Pr (Praseodymium) element
        button_pr = ttk.Button(frame_elements, text="Pr")
        button_pr.grid(row=7, column=4, padx=pad_x, pady=pad_y)

        # Creating the Nd (Neodymium) element
        button_nd = ttk.Button(frame_elements, text="Nd")
        button_nd.grid(row=7, column=5, padx=pad_x, pady=pad_y)

        # Creating the Pm (Promethium) element
        button_pm = ttk.Button(frame_elements, text="Pm")
        button_pm.grid(row=7, column=6, padx=pad_x, pady=pad_y)

        # Creating the Sm (Samarium) element
        button_sm = ttk.Button(frame_elements, text="Sm")
        button_sm.grid(row=7, column=7, padx=pad_x, pady=pad_y)

        # Creating the Eu (Europium) element
        button_eu = ttk.Button(frame_elements, text="Eu")
        button_eu.grid(row=7, column=8, padx=pad_x, pady=pad_y)

        # Creating the Gd (Gadolinium) element
        button_gd = ttk.Button(frame_elements, text="Gd")
        button_gd.grid(row=7, column=9, padx=pad_x, pady=pad_y)

        # Creating the Tb (Terbium) element
        button_tb = ttk.Button(frame_elements, text="Tb")
        button_tb.grid(row=7, column=10, padx=pad_x, pady=pad_y)

        # Creating the Dy (Dysprosium) element
        button_dy = ttk.Button(frame_elements, text="Dy")
        button_dy.grid(row=7, column=11, padx=pad_x, pady=pad_y)

        # Creating the Ho (Holmium) element
        button_ho = ttk.Button(frame_elements, text="Ho")
        button_ho.grid(row=7, column=12, padx=pad_x, pady=pad_y)

        # Creating the Er (Erbium) element
        button_er = ttk.Button(frame_elements, text="Er")
        button_er.grid(row=7, column=13, padx=pad_x, pady=pad_y)

        # Creating the Tm (Thulium) element
        button_tm = ttk.Button(frame_elements, text="Tm")
        button_tm.grid(row=7, column=14, padx=pad_x, pady=pad_y)

        # Creating the Yb (Ytterbium) element
        button_yb = ttk.Button(frame_elements, text="Yb")
        button_yb.grid(row=7, column=15, padx=pad_x, pady=pad_y)

        # Creating the Lu (Lutetium) element
        button_lu = ttk.Button(frame_elements, text="Lu")
        button_lu.grid(row=7, column=16, padx=pad_x, pady=pad_y)

        # Creating the Ac (Actinium) element
        button_ac = ttk.Button(frame_elements, text="Ac")
        button_ac.grid(row=8, column=2, padx=pad_x, pady=pad_y)

        # Creating the Th (Thorium) element
        button_th = ttk.Button(frame_elements, text="Th")
        button_th.grid(row=8, column=3, padx=pad_x, pady=pad_y)

        # Creating the Pa (Protactinium) element
        button_pa = ttk.Button(frame_elements, text="Pa")
        button_pa.grid(row=8, column=4, padx=pad_x, pady=pad_y)

        # Creating the U (Uranium) element
        button_u = ttk.Button(frame_elements, text="U")
        button_u.grid(row=8, column=5, padx=pad_x, pady=pad_y)

        # Creating the Np (Neptunium) element
        button_np = ttk.Button(frame_elements, text="Np")
        button_np.grid(row=8, column=6, padx=pad_x, pady=pad_y)

        # Creating the Pu (Plutonium) element
        button_pu = ttk.Button(frame_elements, text="Pu")
        button_pu.grid(row=8, column=7, padx=pad_x, pady=pad_y)

        # Creating the Am (Americium) element
        button_am = ttk.Button(frame_elements, text="Am")
        button_am.grid(row=8, column=8, padx=pad_x, pady=pad_y)

        # Creating the Cm (Curium) element
        button_cm = ttk.Button(frame_elements, text="Cm")
        button_cm.grid(row=8, column=9, padx=pad_x, pady=pad_y)

        # Creating the Bk (Berkelium) element
        button_bk = ttk.Button(frame_elements, text="Bk")
        button_bk.grid(row=8, column=10, padx=pad_x, pady=pad_y)

        # Creating the Cf (Californium) element
        button_cf = ttk.Button(frame_elements, text="Cf")
        button_cf.grid(row=8, column=11, padx=pad_x, pady=pad_y)

        # Creating the Es (Einsteinium) element
        button_es = ttk.Button(frame_elements, text="Es")
        button_es.grid(row=8, column=12, padx=pad_x, pady=pad_y)

        # Creating the Fm (Fermium) element
        button_fm = ttk.Button(frame_elements, text="Fm")
        button_fm.grid(row=8, column=13, padx=pad_x, pady=pad_y)

        # Creating the Md (Mendelevium) element
        button_md = ttk.Button(frame_elements, text="Md")
        button_md.grid(row=8, column=14, padx=pad_x, pady=pad_y)

        # Creating the No (Nobelium) element
        button_no = ttk.Button(frame_elements, text="No")
        button_no.grid(row=8, column=15, padx=pad_x, pady=pad_y)

        # Creating the Lr (Lawrencium) element
        button_lr = ttk.Button(frame_elements, text="Lr")
        button_lr.grid(row=8, column=16, padx=pad_x, pady=pad_y)

        # Creating the label Atomic number and an entry
        basic_data_atomic_number = ttk.Label(frame_basic_data, text="Atomic Number (Z)")
        basic_data_atomic_number.grid(row=0, column=0, padx=pad_x, pady=pad_y)
        entry_atomic_number = ttk.Entry(frame_basic_data, width=entry_box)
        entry_atomic_number.grid(row=0, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_atomic_number.config(state="readonly")

        # Creating the label Symbol and an entry
        basic_data_symbol = ttk.Label(frame_basic_data, text="Symbol")
        basic_data_symbol.grid(row=1, column=0, padx=pad_x, pady=pad_y)
        entry_symbol = ttk.Entry(frame_basic_data, width=entry_box)
        entry_symbol.grid(row=1, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_symbol.config(state="readonly")

        # Creating the label Name and an entry
        basic_data_name = ttk.Label(frame_basic_data, text="Name")
        basic_data_name.grid(row=2, column=0, padx=pad_x, pady=pad_y)
        entry_name = ttk.Entry(frame_basic_data, width=entry_box)
        entry_name.grid(row=2, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_name.config(state="readonly")

        # Creating the label Atomic weight and an entry
        basic_data_atomic_number = ttk.Label(frame_basic_data, text="(Standard) Atomic weight (Aᵣ)")
        basic_data_atomic_number.grid(row=3, column=0, padx=pad_x, pady=pad_y)
        entry_atomic_number = ttk.Entry(frame_basic_data, width=entry_box)
        entry_atomic_number.grid(row=3, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_atomic_number.config(state="readonly")

        # Creating the label Group and an entry
        data_group = ttk.Label(frame_data, text="Group")
        data_group.grid(row=0, column=0, padx=1, pady=1)
        entry_group = ttk.Entry(frame_data, width=entry_box)
        entry_group.grid(row=0, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_group.config(state="readonly")

        # Creating the label Period and an entry
        data_period = ttk.Label(frame_data, text="Period")
        data_period.grid(row=1, column=0, padx=1, pady=1)
        entry_period = ttk.Entry(frame_data, width=entry_box)
        entry_period.grid(row=1, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_period.config(state="readonly")

        # Creating the label Block and an entry
        data_block = ttk.Label(frame_data, text="Block")
        data_block.grid(row=2, column=0, padx=1, pady=1)
        entry_block = ttk.Entry(frame_data, width=entry_box)
        entry_block.grid(row=2, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_block.config(state="readonly")

        # Creating the label Electron configuration and an entry
        data_electron_config = ttk.Label(frame_data, text="Electron configuration")
        data_electron_config.grid(row=3, column=0, padx=1, pady=1)
        entry_electron_config = ttk.Entry(frame_data, width=entry_box)
        entry_electron_config.grid(row=3, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_electron_config.config(state="readonly")

        # Creating the label Electrons per shell configuration and an entry
        data_electron_shell = ttk.Label(frame_data, text="Electrons per shell")
        data_electron_shell.grid(row=4, column=0, padx=1, pady=1)
        entry_electron_shell = ttk.Entry(frame_data, width=entry_box)
        entry_electron_shell.grid(row=4, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_electron_shell.config(state="readonly")

        # Creating the label Phase at STP and an entry
        physical_properties_stp = ttk.Label(frame_physical_properties, text="Phase at STP")
        physical_properties_stp.grid(row=0, column=0, padx=1, pady=1)
        entry_stp = ttk.Entry(frame_physical_properties, width=entry_box)
        entry_stp.grid(row=0, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_stp.config(state="readonly")

        # Creating the label Melting point and an entry
        physical_properties_melting_point = ttk.Label(frame_physical_properties, text="Melting point [K]")
        physical_properties_melting_point.grid(row=1, column=0, padx=1, pady=1)
        entry_melting_point = ttk.Entry(frame_physical_properties, width=entry_box)
        entry_melting_point.grid(row=1, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_melting_point.config(state="readonly")

        # Creating the label Boiling point and an entry
        physical_properties_boiling_point = ttk.Label(frame_physical_properties, text="Boiling point [K]")
        physical_properties_boiling_point.grid(row=2, column=0, padx=1, pady=1)
        entry_boiling_point = ttk.Entry(frame_physical_properties, width=entry_box)
        entry_boiling_point.grid(row=2, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_boiling_point.config(state="readonly")

        # Creating the label Density at STP and an entry
        physical_properties_density = ttk.Label(frame_physical_properties, text="Density at STP [g/L]")
        physical_properties_density.grid(row=3, column=0, padx=1, pady=1)
        entry_density = ttk.Entry(frame_physical_properties, width=entry_box)
        entry_density.grid(row=3, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_density.config(state="readonly")

        # Creating the label Triple point and an entry
        physical_properties_triple_point = ttk.Label(frame_physical_properties, text="Triple point [K | Pa]")
        physical_properties_triple_point.grid(row=4, column=0, padx=1, pady=1)
        entry_triple_point = ttk.Entry(frame_physical_properties, width=entry_box)
        entry_triple_point.grid(row=4, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_triple_point.config(state="readonly")

        # Creating the label Critical point and an entry
        physical_properties_critical_point = ttk.Label(frame_physical_properties, text="Critical point [K | Pa]")
        physical_properties_critical_point.grid(row=0, column=2, padx=1, pady=1)
        entry_critical_point = ttk.Entry(frame_physical_properties, width=entry_box)
        entry_critical_point.grid(row=0, column=3, padx=pad_box_x, pady=pad_box_y)
        entry_critical_point.config(state="readonly")

        # Creating the label Heat of fusion and an entry
        physical_properties_heat_fusion = ttk.Label(frame_physical_properties, text="Heat of fusion [kJ/mol]")
        physical_properties_heat_fusion.grid(row=1, column=2, padx=1, pady=1)
        entry_heat_fusion = ttk.Entry(frame_physical_properties, width=entry_box)
        entry_heat_fusion.grid(row=1, column=3, padx=pad_box_x, pady=pad_box_y)
        entry_heat_fusion.config(state="readonly")

        # Creating the label Heat of vaporization and an entry
        physical_properties_heat_vapor = ttk.Label(frame_physical_properties, text="Heat of vaporization [kJ/mol]")
        physical_properties_heat_vapor.grid(row=2, column=2, padx=1, pady=1)
        entry_heat_vapor = ttk.Entry(frame_physical_properties, width=entry_box)
        entry_heat_vapor.grid(row=2, column=3, padx=pad_box_x, pady=pad_box_y)
        entry_heat_vapor.config(state="readonly")

        # Creating the label Molar heat capacity and an entry
        physical_properties_molar_heat = ttk.Label(frame_physical_properties, text="Molar heat capacity [J/(mol·K)]")
        physical_properties_molar_heat.grid(row=3, column=2, padx=1, pady=1)
        entry_molar_heat = ttk.Entry(frame_physical_properties, width=entry_box)
        entry_molar_heat.grid(row=3, column=3, padx=pad_box_x, pady=pad_box_y)
        entry_molar_heat.config(state="readonly")

        # Creating the label Vapor pressure and an entry
        physical_properties_vapor_pres = ttk.Label(frame_physical_properties, text="Vapor pressure 10 kPa at at T [K]")
        physical_properties_vapor_pres.grid(row=4, column=2, padx=1, pady=1)
        entry_vapor_pres = ttk.Entry(frame_physical_properties, width=entry_box)
        entry_vapor_pres.grid(row=4, column=3, padx=pad_box_x, pady=pad_box_y)
        entry_vapor_pres.config(state="readonly")

        # Creating the label Oxidation states and an entry
        atomic_properties_oxidation = ttk.Label(frame_atomic_properties, text="Oxidation states")
        atomic_properties_oxidation.grid(row=0, column=0, padx=1, pady=1)
        entry_oxidation = ttk.Entry(frame_atomic_properties, width=entry_box)
        entry_oxidation.grid(row=0, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_oxidation.config(state="readonly")

        # Creating the label Electronegativity and an entry
        atomic_properties_electronegative = ttk.Label(frame_atomic_properties, text="Electronegativity (Pauling scale)")
        atomic_properties_electronegative.grid(row=1, column=0, padx=1, pady=1)
        entry_electronegative = ttk.Entry(frame_atomic_properties, width=entry_box)
        entry_electronegative.grid(row=1, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_electronegative.config(state="readonly")

        # Creating the label Ionization energies and an entry
        atomic_properties_ionization = ttk.Label(frame_atomic_properties, text="Ionization energies [kJ/mol]")
        atomic_properties_ionization.grid(row=2, column=0, padx=1, pady=1)
        entry_ionization = ttk.Entry(frame_atomic_properties, width=entry_box)
        entry_ionization.grid(row=2, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_ionization.config(state="readonly")

        # Creating the label Covalent radius and an entry
        atomic_properties_covalent_radius = ttk.Label(frame_atomic_properties, text="Covalent radius [pm]")
        atomic_properties_covalent_radius.grid(row=3, column=0, padx=1, pady=1)
        entry_covalent_radius = ttk.Entry(frame_atomic_properties, width=entry_box)
        entry_covalent_radius.grid(row=3, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_covalent_radius.config(state="readonly")

        # Creating the label Van der Waals radius and an entry
        atomic_properties_waals = ttk.Label(frame_atomic_properties, text="Van der Waals radius [pm]")
        atomic_properties_waals.grid(row=4, column=0, padx=1, pady=1)
        entry_waals = ttk.Entry(frame_atomic_properties, width=entry_box)
        entry_waals.grid(row=4, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_waals.config(state="readonly")

        # Creating the label Natural occurrence and an entry
        other_properties_natural = ttk.Label(frame_other_properties, text="Natural occurrence")
        other_properties_natural.grid(row=0, column=0, padx=1, pady=1)
        entry_natural = ttk.Entry(frame_other_properties, width=entry_box)
        entry_natural.grid(row=0, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_natural.config(state="readonly")

        # Creating the label Crystal structure and an entry
        other_properties_crystal = ttk.Label(frame_other_properties, text="Crystal structure")
        other_properties_crystal.grid(row=1, column=0, padx=1, pady=1)
        entry_crystal = ttk.Entry(frame_other_properties, width=entry_box)
        entry_crystal.grid(row=1, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_crystal.config(state="readonly")

        # Creating the label Speed of sound and an entry
        other_properties_speed_sound = ttk.Label(frame_other_properties, text="Speed of sound [m/s]")
        other_properties_speed_sound.grid(row=2, column=0, padx=1, pady=1)
        entry_speed_sound = ttk.Entry(frame_other_properties, width=entry_box)
        entry_speed_sound.grid(row=2, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_speed_sound.config(state="readonly")

        # Creating the label Thermal conductivity and an entry
        other_properties_thermal_cond = ttk.Label(frame_other_properties, text="Thermal conductivity")
        other_properties_thermal_cond.grid(row=3, column=0, padx=1, pady=1)
        entry_thermal_cond = ttk.Entry(frame_other_properties, width=entry_box)
        entry_thermal_cond.grid(row=3, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_thermal_cond.config(state="readonly")

        # Creating the label Magnetic ordering and an entry
        other_properties_magnetic_ord = ttk.Label(frame_other_properties, text="Magnetic ordering")
        other_properties_magnetic_ord.grid(row=4, column=0, padx=1, pady=1)
        entry_magnetic_ord = ttk.Entry(frame_other_properties, width=entry_box)
        entry_magnetic_ord.grid(row=4, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_magnetic_ord.config(state="readonly")

        # Creating the label Magnetic ordering and an entry
        other_properties_magnetic_ord = ttk.Label(frame_other_properties, text="Magnetic susceptibility")
        other_properties_magnetic_ord.grid(row=5, column=0, padx=17, pady=1)
        entry_magnetic_ord = ttk.Entry(frame_other_properties, width=entry_box)
        entry_magnetic_ord.grid(row=5, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_magnetic_ord.config(state="readonly")

        # Creating the label Discovery and an entry
        history_discovery = ttk.Label(frame_history, text="Discovery by")
        history_discovery.grid(row=0, column=0, padx=17, pady=1)
        entry_discovery = ttk.Entry(frame_history, width=entry_box)
        entry_discovery.grid(row=0, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_discovery.config(state="readonly")

        # Creating the label Year and an entry
        history_year = ttk.Label(frame_history, text="Year")
        history_year.grid(row=1, column=0, padx=17, pady=1)
        entry_year = ttk.Entry(frame_history, width=entry_box)
        entry_year.grid(row=1, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_year.config(state="readonly")

        # Creating the label Nationality and an entry
        history_nationality = ttk.Label(frame_history, text="Nationality")
        history_nationality.grid(row=2, column=0, padx=17, pady=1)
        entry_nationality = ttk.Entry(frame_history, width=entry_box)
        entry_nationality.grid(row=2, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_nationality.config(state="readonly")

        # Creating the label Alma mater and an entry
        history_alma_mater = ttk.Label(frame_history, text="Alma mater")
        history_alma_mater.grid(row=3, column=0, padx=17, pady=1)
        entry_alma_mater = ttk.Entry(frame_history, width=entry_box)
        entry_alma_mater.grid(row=3, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_alma_mater.config(state="readonly")

        # Creating the label Fields and an entry
        history_fields = ttk.Label(frame_history, text="Fields")
        history_fields.grid(row=4, column=0, padx=17, pady=1)
        entry_field = ttk.Entry(frame_history, width=entry_box)
        entry_field.grid(row=4, column=1, padx=pad_box_x, pady=pad_box_y)
        entry_field.config(state="readonly")

        # Creating the label Born | Died and an entry
        history_born_died = ttk.Label(frame_history, text="Born | Died")
        history_born_died.grid(row=5, column=0, padx=17, pady=1)
        born_died = ttk.Entry(frame_history, width=entry_box)
        born_died.grid(row=5, column=1, padx=pad_box_x, pady=pad_box_y)
        born_died.config(state="readonly")

        # Creating the label Dummy for frame_image_
        frame_image_dummy = ttk.Label(frame_image)
        frame_image_dummy.grid(row=0, column=0, padx=263, pady=60)
