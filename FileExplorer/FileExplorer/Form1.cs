using System.Text;

namespace FileExplorer
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private TreeNode FindTreeNodeByFullPath(TreeNodeCollection collection, string path, StringComparison comparison = StringComparison.InvariantCultureIgnoreCase)
        {
            var found_node = collection.Cast<TreeNode>().FirstOrDefault(node => string.Equals(node.FullPath, path, comparison));
            if (found_node == null)
            {
                foreach (var child_node in collection.Cast<TreeNode>())
                {
                    var found_childNode = FindTreeNodeByFullPath(child_node.Nodes, path, comparison);
                    if (found_childNode != null)
                        return found_childNode;
                }
            }
            return found_node;
        }

        private void AddPathRecursive(string path, TreeNode node)
        {
            path = path.Replace("\\", "/").Replace("://", ":/");
            string[] folder_inPath = path.Split('/');
            string edited_path = "";
            StringBuilder sb = new StringBuilder();
            if (folder_inPath.Length > 0)
            {
                for (int i = 1; i < folder_inPath.Length; i++)
                    sb.Append(folder_inPath[i] + "/");
                edited_path = sb.ToString();
                edited_path = edited_path.Remove(edited_path.ToCharArray().Length - 1);
            }

            if (!string.IsNullOrEmpty(edited_path))
            {
                TreeNode child_node = new TreeNode(edited_path.Split('/')[0]);
                node.Nodes.Add(child_node);
                AddPathRecursive(edited_path, child_node);
            }
            treeView1.ExpandAll();
        }

        void setup()
        {
            foreach (DriveInfo drive in DriveInfo.GetDrives())
            {
                TreeNode node = new TreeNode(drive.Name);
                treeView1.Nodes.Add(node);
            }
            string current_path = Application.StartupPath;
            textBox1.Text = current_path;
            string current_drive = current_path.Split('\\')[0];
            TreeNode drive_node = FindTreeNodeByFullPath(treeView1.Nodes, current_drive + "\\");
            if (drive_node != null)
                AddPathRecursive(current_path, drive_node);

            TreeNode current_node = FindTreeNodeByFullPath(treeView1.Nodes, FindTreeNode_Format(current_path));
            treeView1.SelectedNode = null;
            if (current_node != null)
                treeView1.SelectedNode = current_node;
            else
                MessageBox.Show("Not found " + FindTreeNode_Format(current_path));
        }

        string FindTreeNode_Format(string path)
        {
            path = path.Remove(path.ToCharArray().Length - 1);
            return path.Replace("\\", "/").Replace(":", ":/").Replace("/", "\\");
        }

        string TreeNodePathToNormal(string path)
        {
            return path.Replace("\\", "/").Replace(":/", ":") + "/";
        }

        void ScanDir(string current_path)
        {
            int file_count = 0;
            int folder_count = 0;
            foreach (string dir in Directory.GetDirectories(current_path))
            {
                DirectoryInfo info = new DirectoryInfo(dir);
                ListViewItem item = new ListViewItem(Path.GetFileName(dir));
                item.SubItems.Add(info.Attributes.ToString());
                item.SubItems.Add("Size");
                foreach (string date in new string[] { info.CreationTime.ToString(), info.LastAccessTime.ToString(), info.LastWriteTime.ToString() })
                    item.SubItems.Add(date);
                listView1.Items.Add(item);

                string node_path = FindTreeNode_Format(textBox1.Text) + "\\" + info.Name;
                TreeNode existed_node = FindTreeNodeByFullPath(treeView1.Nodes, node_path);
                if (existed_node == null)
                {
                    TreeNode _node = new TreeNode(info.Name);
                    TreeNode selected_node = treeView1.SelectedNode;
                    selected_node.Nodes.Add(_node);
                    selected_node.Expand();
                }
                folder_count++;
            }
            foreach (string file in Directory.GetFiles(current_path))
            {
                FileInfo info = new FileInfo(file);
                ListViewItem item = new ListViewItem(Path.GetFileName(file));
                item.SubItems.Add(info.Attributes.ToString());
                item.SubItems.Add("Size");
                foreach (string date in new string[] { info.CreationTime.ToString(), info.LastAccessTime.ToString(), info.LastWriteTime.ToString() })
                    item.SubItems.Add(date);
                //Icon icon = System.Drawing.Icon.ExtractAssociatedIcon(file);
                listView1.Items.Add(item);
                file_count++;
            }
            toolStripStatusLabel1.Text = string.Format("Folder[{0}] File[{1}]", folder_count, file_count);
        }

        private void Form1_Load(object sender, EventArgs e)
        {
            setup();
        }

        private void treeView1_AfterSelect(object sender, TreeViewEventArgs e)
        {
            listView1.Items.Clear();
            string current_path = TreeNodePathToNormal(treeView1.SelectedNode.FullPath);
            textBox1.Text = current_path.Replace("/", "\\");
            ScanDir(current_path);
        }
    }
}