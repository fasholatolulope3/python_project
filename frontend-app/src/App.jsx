import React, { useState, useEffect } from 'react';
import { 
  BarChart3, 
  Cpu, 
  Ticket as TicketIcon, 
  Globe, 
  Plus, 
  CheckCircle2, 
  AlertCircle, 
  Clock, 
  ShieldCheck 
} from 'lucide-react';
import api from './api';

function App() {
  const [activeTab, setActiveTab] = useState('dashboard');
  const [assets, setAssets] = useState([]);
  const [tickets, setTickets] = useState([]);
  const [services, setServices] = useState([]);
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    fetchData();
  }, []);

  const fetchData = async () => {
    try {
      setLoading(true);
      const [assetsRes, ticketsRes, servicesRes] = await Promise.all([
        api.get('assets/'),
        api.get('tickets/'),
        api.get('services/'),
      ]);
      setAssets(assetsRes.data);
      setTickets(ticketsRes.data);
      setServices(servicesRes.data);
    } catch (error) {
      console.error("Error fetching data:", error);
    } finally {
      setLoading(false);
    }
  };

  const Sidebar = () => (
    <div className="sidebar">
      <div className="sidebar-brand">
        VEMRE <span style={{ color: 'white' }}>SUPPORT</span>
      </div>
      <nav>
        <button 
          onClick={() => setActiveTab('dashboard')} 
          className={`nav-link ${activeTab === 'dashboard' ? 'active' : ''}`}
        >
          <BarChart3 size={20} /> Dashboard
        </button>
        <button 
          onClick={() => setActiveTab('assets')} 
          className={`nav-link ${activeTab === 'assets' ? 'active' : ''}`}
        >
          <Cpu size={20} /> IT Assets
        </button>
        <button 
          onClick={() => setActiveTab('tickets')} 
          className={`nav-link ${activeTab === 'tickets' ? 'active' : ''}`}
        >
          <TicketIcon size={20} /> Support Tickets
        </button>
        <button 
          onClick={() => setActiveTab('services')} 
          className={`nav-link ${activeTab === 'services' ? 'active' : ''}`}
        >
          <Globe size={20} /> Service Desk
        </button>
      </nav>
      
      <div style={{ marginTop: 'auto' }}>
        <div className="card" style={{ padding: '1rem', background: '#0f172a', marginBottom: 0 }}>
          <div style={{ display: 'flex', alignItems: 'center', gap: '0.75rem' }}>
            <div style={{ padding: '0.5rem', background: '#334155', borderRadius: '50%' }}>
              <ShieldCheck size={20} color="#6366f1" />
            </div>
            <div>
              <p style={{ fontSize: '0.8rem', fontWeight: 600 }}>System Secure</p>
              <p className="text-muted" style={{ fontSize: '0.7rem' }}>Monitoring Active</p>
            </div>
          </div>
        </div>
      </div>
    </div>
  );

  const Dashboard = () => (
    <div>
      <div className="top-bar">
        <h1>Overview</h1>
        <p className="text-muted">Welcome back to Vemre IT Command Center</p>
      </div>

      <div className="stats-grid">
        <div className="card">
          <p className="text-muted">Total Assets</p>
          <h2>{assets.length}</h2>
          <div style={{ color: '#10b981', fontSize: '0.8rem' }}>+2 this month</div>
        </div>
        <div className="card">
          <p className="text-muted">Open Tickets</p>
          <h2 style={{ color: '#f87171' }}>{tickets.filter(t => t.status !== 'CLOSED').length}</h2>
          <div style={{ color: '#f87171', fontSize: '0.8rem' }}>{tickets.filter(t => t.priority === 'URGENT').length} Urgent</div>
        </div>
        <div className="card">
          <p className="text-muted">Services Status</p>
          <h2 style={{ color: '#22d3ee' }}>{services.filter(s => s.status).length}/{services.length}</h2>
          <div style={{ color: '#22d3ee', fontSize: '0.8rem' }}>All primary systems UP</div>
        </div>
      </div>

      <div className="card">
        <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1.5rem' }}>
          <h3>Recent Support Tickets</h3>
          <button className="btn btn-primary" onClick={() => setActiveTab('tickets')}>View All</button>
        </div>
        <table>
          <thead>
            <tr>
              <th>Issue</th>
              <th>Asset</th>
              <th>Priority</th>
              <th>Status</th>
            </tr>
          </thead>
          <tbody>
            {tickets.slice(0, 5).map(ticket => (
              <tr key={ticket.id}>
                <td style={{ fontWeight: 600 }}>{ticket.title}</td>
                <td className="text-muted">{ticket.asset_name}</td>
                <td><span className={`tag tag-${ticket.priority.toLowerCase()}`}>{ticket.priority}</span></td>
                <td>
                  <div style={{ display: 'flex', alignItems: 'center', gap: '0.5rem' }}>
                    {ticket.status === 'RESOLVED' ? <CheckCircle2 size={16} color="#10b981" /> : <Clock size={16} color="#fbbf24" />}
                    {ticket.status}
                  </div>
                </td>
              </tr>
            ))}
          </tbody>
        </table>
      </div>
    </div>
  );

  const Assets = () => (
    <div>
      <div className="top-bar">
        <h1>IT Assets</h1>
        <button className="btn btn-primary"><Plus size={18} /> Add New Asset</button>
      </div>
      <div className="stats-grid">
        {assets.map(asset => (
          <div key={asset.id} className="card">
            <div style={{ display: 'flex', justifyContent: 'space-between', marginBottom: '1rem' }}>
              <Cpu color="#6366f1" />
              <span className="text-muted" style={{ fontSize: '0.75rem' }}>{asset.asset_type}</span>
            </div>
            <h3>{asset.name}</h3>
            <p className="text-muted" style={{ marginBottom: '1rem' }}>S/N: {asset.serial_number}</p>
            <div style={{ fontSize: '0.8rem' }}>Assigned to: <span style={{ color: 'white' }}>{asset.assigned_to || 'Unassigned'}</span></div>
          </div>
        ))}
      </div>
    </div>
  );

  return (
    <div className="dashboard-container">
      <Sidebar />
      <main className="main-content">
        {loading ? (
          <div style={{ display: 'flex', height: '80vh', alignItems: 'center', justifyContent: 'center' }}>
            <div className="text-muted">Loading System Data...</div>
          </div>
        ) : (
          <>
            {activeTab === 'dashboard' && <Dashboard />}
            {activeTab === 'assets' && <Assets />}
            {activeTab === 'tickets' && <div className="card"><h2>Support Ticket Management</h2><p className="text-muted">Ticket module is ready for expanding.</p></div>}
            {activeTab === 'services' && <div className="card"><h2>Service Status Desk</h2><p className="text-muted">Service monitoring is active.</p></div>}
          </>
        )}
      </main>
    </div>
  );
}

export default App;
