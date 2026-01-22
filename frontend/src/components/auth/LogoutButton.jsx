import React from 'react';
import { useAuth } from '../../contexts/AuthContext';
import { useNavigate } from 'react-router-dom';
import { Button } from '../ui/button';
import { LogOut } from 'lucide-react';

const LogoutButton = ({ variant = "outline", size = "sm", showIcon = true, children }) => {
  const { logout } = useAuth();
  const navigate = useNavigate();

  const handleLogout = () => {
    logout();
    navigate('/login');
  };

  return (
    <Button
      variant={variant}
      size={size}
      onClick={handleLogout}
      className="flex items-center gap-2"
    >
      {showIcon && <LogOut className="w-4 h-4" />}
      {children || 'Logout'}
    </Button>
  );
};

export default LogoutButton;